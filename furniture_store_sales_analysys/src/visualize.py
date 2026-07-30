"""
visualize.py
------------
Generates the key charts used in the analysis notebook and README,
saved as PNG files to the visuals/ directory.

Usage:
    python src/visualize.py
        --input data/processed/cleaned_sessions.csv
        --outdir visuals
"""

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.dpi"] = 130


def plot_monthly_trend(df: pd.DataFrame, outdir: str):
    monthly = df.groupby("order_month").agg(
        sessions=("ga_session_id", "count"),
        orders=("purchased", "sum"),
        revenue=("revenue", "sum"),
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax2 = ax1.twinx()

    ax1.bar(monthly["order_month"], monthly["revenue"], color="#4C72B0", alpha=0.7, label="Revenue")
    ax2.plot(monthly["order_month"], monthly["orders"], color="#DD8452", marker="o", linewidth=2, label="Orders")

    ax1.set_ylabel("Revenue ($)")
    ax2.set_ylabel("Orders")
    ax1.set_xlabel("Month")
    ax1.set_title("Monthly Revenue and Orders")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "monthly_trend.png"))
    plt.close(fig)


def plot_conversion_by_device(df: pd.DataFrame, outdir: str):
    rate = df.groupby("device")["purchased"].mean().sort_values(ascending=False) * 100

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.barplot(x=rate.index, y=rate.values, ax=ax)
    ax.set_ylabel("Conversion rate (%)")
    ax.set_xlabel("Device")
    ax.set_title("Conversion Rate by Device")
    for i, v in enumerate(rate.values):
        ax.text(i, v + 0.05, f"{v:.2f}%", ha="center")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "conversion_by_device.png"))
    plt.close(fig)


def plot_revenue_by_category(df: pd.DataFrame, outdir: str):
    rev = df[df["purchased"]].groupby("product_category")["revenue"].sum().sort_values()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=rev.values, y=rev.index, ax=ax, color="#4C72B0")
    ax.set_xlabel("Revenue ($)")
    ax.set_ylabel("Product category")
    ax.set_title("Total Revenue by Product Category")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "revenue_by_category.png"))
    plt.close(fig)


def plot_top_countries(df: pd.DataFrame, outdir: str, n=10):
    top = df["country"].value_counts().head(n)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=top.values, y=top.index, ax=ax, color="#55A868")
    ax.set_xlabel("Sessions")
    ax.set_ylabel("Country")
    ax.set_title(f"Top {n} Countries by Session Volume")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "top_countries.png"))
    plt.close(fig)


def plot_traffic_channel_performance(df: pd.DataFrame, outdir: str):
    perf = df.groupby("traffic_channel").agg(
        sessions=("ga_session_id", "count"),
        conversion_rate=("purchased", "mean"),
    ).reset_index()
    perf["conversion_rate"] *= 100

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=perf, x="sessions", y="conversion_rate",
        s=200, hue="traffic_channel", ax=ax, legend=False,
    )
    for _, row in perf.iterrows():
        ax.text(row["sessions"], row["conversion_rate"] + 0.03, row["traffic_channel"], ha="center", fontsize=9)
    ax.set_xlabel("Sessions")
    ax.set_ylabel("Conversion rate (%)")
    ax.set_title("Traffic Channel: Volume vs Conversion Rate")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "traffic_channel_performance.png"))
    plt.close(fig)


def plot_registration_impact(df: pd.DataFrame, outdir: str):
    reg = df.groupby("is_registered")["purchased"].mean() * 100
    reg.index = ["Guest", "Registered"]

    fig, ax = plt.subplots(figsize=(5, 5))
    sns.barplot(x=reg.index, y=reg.values, ax=ax)
    ax.set_ylabel("Conversion rate (%)")
    ax.set_title("Conversion Rate: Guest vs Registered Users")
    for i, v in enumerate(reg.values):
        ax.text(i, v + 0.05, f"{v:.2f}%", ha="center")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "registration_impact.png"))
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate charts for the furniture store analysis.")
    parser.add_argument("--input", default="data/processed/cleaned_sessions.csv")
    parser.add_argument("--outdir", default="visuals")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    df = pd.read_csv(args.input, parse_dates=["order_date"])

    print("Generating charts ...")
    plot_monthly_trend(df, args.outdir)
    plot_conversion_by_device(df, args.outdir)
    plot_revenue_by_category(df, args.outdir)
    plot_top_countries(df, args.outdir)
    plot_traffic_channel_performance(df, args.outdir)
    plot_registration_impact(df, args.outdir)
    print(f"Charts saved to {args.outdir}/")


if __name__ == "__main__":
    main()
