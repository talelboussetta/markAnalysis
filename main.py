import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def round_numbers(df):
    """
    Round numbers according to specific rules:
    - .25 or .50 round down
    - .75 rounds up
    """
    def round_mark(x):
        if x % 1 == 0.25 or x % 1 == 0.50:
            return np.floor(x)
        elif x % 1 == 0.75:
            return np.ceil(x)
        return x

    return df.apply(round_mark)

def clean_data(df):
    """
    Clean the data by removing invalid marks (>20 or <0)
    Returns cleaned data and count of removed values
    """
    valid_mask = (df >= 0) & (df <= 20)
    removed_count = np.sum(~valid_mask)
    return df[valid_mask], removed_count

def calculate_statistics(marks):
    """Calculate basic statistics for the marks"""
    return {
        'mean': marks.mean(),
        'median': marks.median(),
        'std': marks.std(),
        'pass_rate': (marks >= 10).mean() * 100
    }

def create_color_scheme(counts):
    """Create color scheme based on frequency"""
    return ['red' if count > 15 else 'orange' if count > 10 else 'blue'
            for count in counts]

def plot_marks_histogram(marks, stats):
    """Create an enhanced histogram plot with statistics"""
    # Count occurrences for marks from 0 to 20
    bins = list(range(22))  # Create bins for marks 0 to 20
    int_counts, _ = np.histogram(marks, bins=bins)

    # Prepare plot
    plt.figure(figsize=(18, 12))  # Increase figure size
    x_labels = bins[:-1]  # Use bin edges excluding the last one
    bar_colors = create_color_scheme(int_counts)

    # Create main plot
    plt.bar(x_labels, int_counts, color=bar_colors, edgecolor='black', align='center')

    # Add titles and labels
    plt.title(
              'Add your title here', color='purple', fontweight='bold', pad=20, fontsize=16)
    plt.xlabel('marks', fontsize=14)
    plt.ylabel('students', fontsize=14)

    # Add statistics text box
    stats_text = (
        f"Statistiques:\n"
        f"Moyenne: {stats['mean']:.2f}\n"
        f"Médiane: {stats['median']:.2f}\n"
        f"Écart type: {stats['std']:.2f}\n"
        f"Taux de réussite: {stats['pass_rate']:.1f}%"
    )
    plt.text(0.95, 0.95, stats_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    # Add rounding explanation
    plt.text(0, max(int_counts) + 2,
             "5.25 is considered 5 and 5.75 /5.5 are considered to be6\n",
             fontsize=12)

    # Customize appearance
    plt.xticks(x_labels, fontsize=12)
    plt.grid(axis='y', alpha=0.3)

    # Adjust layout padding to ensure all elements fit
    plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.97])  # Adjust margins more generously
    plt.subplots_adjust(top=0.9, bottom=0.1)  # Further adjust top and bottom margins
    plt.figure(figsize=(18, 12), constrained_layout=True)


def main():
    # Define the marks array directly
    marks = [#ADD you're desired numbers here ex
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]


    # Create a pandas DataFrame from the list
    df = pd.Series(marks)

    # Round the data
    df = round_numbers(df)

    # Clean the data
    cleaned_marks, removed_count = clean_data(df)

    # Calculate the statistics
    stats = calculate_statistics(cleaned_marks)

    # Plot the histogram
    plot_marks_histogram(cleaned_marks, stats)

    # Show the plot
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
