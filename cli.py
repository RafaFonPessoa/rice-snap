import argparse
import os
from composer import compose


def main():
    parser = argparse.ArgumentParser(
        prog="rice-snap",
        description="Generate a postcard-style card of your Linux rice.",
    )

    parser.add_argument("image", help="Path to your desktop screenshot")

    parser.add_argument(
        "--seal", default=None, help="Path to a custom seal image (optional)"
    )

    parser.add_argument(
        "--stamp", default=None, help="Path to a custom stamp image (optional)"
    )

    parser.add_argument(
        "--output",
        default=os.path.expanduser("~/Downloads/rice-card.png"),
        help="Output path for the generated card (default: ~/Downloads/rice-card.png)",
    )

    args = parser.parse_args()

    # Resolve asset paths — use defaults if not provided
    seal_path = args.seal or os.path.join(
        os.path.dirname(__file__), "assets", "seal.png"
    )
    stamp_path = args.stamp or os.path.join(
        os.path.dirname(__file__), "assets", "stamp.png"
    )

    compose(
        image_path=args.image,
        seal_path=seal_path,
        stamp_path=stamp_path,
        output_path=args.output,
    )

    print(f"Card saved to {args.output}")


if __name__ == "__main__":
    main()
