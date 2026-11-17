import matplotlib.pyplot as plt
import numpy as np

def plot_lines(y_data: list[float], size:tuple[float, float, str] = (15, 5, "in")): 

    plt.style.use("dark_background")
    
    plt.figure(figsize=size)

    for data in y_data:
        x_data = list(range(len(y_data)))
        plt.plot(x_data, y_data)

    plt.legend()
    plt.show()

def plot_bar(title: str, y_data: list[float], size:tuple[float, float, str] = (15, 5, "in")): 

    x_data = list(range(len(y_data)))
    plt.style.use("dark_background")

    plt.figure(figsize=size)
    bars = plt.bar(x_data, y_data)
    plt.bar_label(# pyright: ignore[reportUnknownMemberType]   
        bars,
        labels=[f"({x}) {y:.1f}" for x, y in zip(x_data, y_data)], 
        padding= 3,  
        fontsize=8)
    plt.title(title)

    plt.show()

def plot_bar_avg_std( title: str, y_data: list[float], size:tuple[float, float, str] = (15, 5, "in")): 
        
        x_data = list(range(len(y_data)))
        plt.style.use("dark_background") 
        
        plt.figure(figsize=size)
        bars = plt.bar(x_data, y_data)
        plt.bar_label(# pyright: ignore[reportUnknownMemberType]   
            bars,
            labels=[f"({x}) {y:.1f}" for x, y in zip(x_data, y_data)], 
            padding= 3,  
            fontsize=8)
        plt.title(title)

        # Moyenne et écart-type
        moyenne = np.mean(y_data)
        ecart_type = np.std(y_data)

        # Lignes
        plt.axhline(
        moyenne,
        linestyle="--",
        linewidth=2,
        label=f"Moyenne : {moyenne:.1f} h"
        )

        plt.axhline(
        moyenne + ecart_type,
        linestyle=":",
        linewidth=1.5,
        label=f"+1 σ : {moyenne + ecart_type:.1f} h"
        )

        plt.axhline(
        moyenne - ecart_type,
        linestyle=":",
        linewidth=1.5,
        label=f"-1 σ : {moyenne - ecart_type:.1f} h"
        )


        plt.show()

        print(f"moy={moyenne}, std={ecart_type}")