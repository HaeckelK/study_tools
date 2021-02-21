import argparse
import csv
import os


def main():
    parser = argparse.ArgumentParser(description="Create import csv file for Anki.")
    # Required
    parser.add_argument(
        "--batch_number",
        type=int,
        help="Batch number to be applied to range of questions added.",
        required=True,
    )
    parser.add_argument("--source", type=str, help="Source used to write question.", required=True)
    parser.add_argument("--chapter", type=int, help="Chapter of source material.", required=True)
    parser.add_argument("--topic", type=str, help="Question topic.", required=True)
    parser.add_argument("--num", type=int, help="Number of questions to create.", required=True)
    # Optional
    parser.add_argument("--sub_topic", type=str, help="Question sub-topic.")
    parser.add_argument(
        "--start_number",
        type=int,
        help="Number from which to begin sequence.",
        default=1,
    )
    parser.add_argument("--tags", type=str, nargs="+", help="Tags to add to created cards.")
    parser.add_argument("--path", type=str, help="Path where files should be saved.", default="data")
    parser.add_argument("--overwrite", action='store_true', help="Overwrite batch file if already exists.")
    args = parser.parse_args()

    batch_number = args.batch_number
    start_number = args.start_number
    source = args.source
    chapter = args.chapter
    topic = args.topic
    sub_topic = args.sub_topic
    path = args.path
    overwrite = args.overwrite

    tags = topic
    if sub_topic:
        tags += " " + sub_topic
    try:
        tags += " ".join(args.tags)
    except TypeError:
        pass

    num_questions = args.num

    filename = os.path.join(path, f"batch_{batch_number}.csv")

    if overwrite is False and os.path.exists(filename):
        print("Filename already exists for this batch, aborting.")
        return

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for i in range(num_questions):
            question_number = i + start_number
            uid = str(batch_number) + "_" + str(question_number)
            writer.writerow(
                [
                    uid,
                    batch_number,
                    source,
                    chapter,
                    topic,
                    sub_topic,
                    question_number,
                    tags,
                ]
            )

    return


if __name__ == "__main__":
    main()
