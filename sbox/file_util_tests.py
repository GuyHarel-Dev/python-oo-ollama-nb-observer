import model_observability.core.file_utils as file_utils




def test():
    folder = r"C:\GH-ORDI\DATA\Data-Model-Observability\output.txt"

    data = "abcdef"
    data = [1, 2, 4, 5]
    data = ["a", "b", "c"]
    data = {"aa": 11, "bb": 222}
    file_utils.write_to_file(folder, data, json_dump=True)


if __name__ == "__main__":
    test()
    pass
