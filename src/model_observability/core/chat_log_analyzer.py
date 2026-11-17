from dataclasses import dataclass
import re as re

from statistics import mean, stdev

from pydantic import BaseModel

from model_observability.core.chat_log_loader import ChatLogLoader, ChatResult
import model_observability.core.json_utils as json_utils


@dataclass
class ChatLogBaseStatistics:
    name: str
    mean: float | None = 0.0
    std: float | None = 0.0


@dataclass
class ChatOptionsStats:
    temp_stats: ChatLogBaseStatistics
    top_k_stats: ChatLogBaseStatistics
    top_p_stats: ChatLogBaseStatistics
    seed_stats: ChatLogBaseStatistics

    @classmethod
    def create(cls) -> "ChatOptionsStats":
        return cls(
            temp_stats=ChatLogBaseStatistics("temp_stats"),
            top_k_stats=ChatLogBaseStatistics("top_k_stats"),
            top_p_stats=ChatLogBaseStatistics("top_p_stats"),
            seed_stats=ChatLogBaseStatistics("seed_stats"),
        )


class ChatContentStats(BaseModel):
    content_samples: int = 0
    content_len_mean: float = 0.0
    content_len_std: float = 0.0
    content_json_keys_mean: float = 0.0
    content_json_keys_std: float = 0.0


class ChatLogFileStats(BaseModel):
    options_stats: ChatOptionsStats
    content_stats: ChatContentStats


class ChatLogAnalyzer:

    def calc_content_stats(self, chat_results: list[ChatResult]) -> ChatContentStats:

        content_stats = ChatContentStats()
        content_stats.content_samples = len(chat_results)

        if content_stats.content_samples < 2:
            return content_stats

        content_lengths: list[int] = []
        content_json_keys: list[int] = []

        for r in chat_results:
            content = r.chat_response.content or ""
            content_lengths.append(len(content))
            content_json_keys.append(len(json_utils.extract_key_values(content)))

        content_stats.content_len_mean = mean(content_lengths)
        content_stats.content_len_std = stdev(content_lengths)

        content_stats.content_json_keys_mean = mean(content_json_keys)
        content_stats.content_json_keys_std = stdev(content_json_keys)

        return content_stats

    def analyze_log_file(self, chat_results: list[ChatResult]) -> ChatLogFileStats:

        options_stats = self.calc_options_stats(chat_results=chat_results)
        contents_stats = self.calc_content_stats(chat_results=chat_results)

        return ChatLogFileStats(
            options_stats=options_stats, content_stats=contents_stats
        )

    def analyze_log_files(self, log_file_folder: str):

        loader = ChatLogLoader(log_file_folder)

        log_files_results = loader.load_log_file_folder()

        log_file_stats: list[ChatLogFileStats] = []

        for file_name_key in log_files_results:
            chat_results = log_files_results[file_name_key]
            chat_log_file_stats = self.analyze_log_file(chat_results)
            log_file_stats.append(chat_log_file_stats)

        [print(stats.content_stats.model_dump()) for stats in log_file_stats]

    def calc_options_stats(self, chat_results: list[ChatResult]) -> ChatOptionsStats:
        options_stats = ChatOptionsStats.create()

        # temperature stats
        options_stats.temp_stats.mean = mean(
            [entry.chat_options.temperature for entry in chat_results]
        )
        options_stats.temp_stats.std = stdev(
            [entry.chat_options.temperature for entry in chat_results]
        )

        # top_k stats
        options_stats.top_k_stats.mean = mean(
            [entry.chat_options.top_k for entry in chat_results]
        )
        options_stats.top_k_stats.std = stdev(
            [entry.chat_options.top_k for entry in chat_results]
        )

        # top_p stats
        options_stats.top_p_stats.mean = mean(
            [entry.chat_options.top_p for entry in chat_results]
        )
        options_stats.top_p_stats.std = stdev(
            [entry.chat_options.top_p for entry in chat_results]
        )

        # seed stats (None by default)
        seed_values = [
            entry.chat_options.seed
            for entry in chat_results
            if entry.chat_options.seed is not None
        ]

        if seed_values:
            options_stats.seed_stats.mean = mean(seed_values)
            options_stats.seed_stats.mean = stdev(seed_values)

        return options_stats


"""


"""
