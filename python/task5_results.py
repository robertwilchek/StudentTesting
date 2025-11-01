"""Sample script that sorts students from a CSV file by last name descending."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

DATA_PATH = Path(__file__).with_name("students.csv")


@dataclass(frozen=True)
class Student:
    """Model a single student record."""

    first_name: str
    last_name: str
    grade: str


def load_students(csv_path: Path = DATA_PATH) -> List[Student]:
    """Load student rows from *csv_path* and return them as Student objects."""

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            Student(
                first_name=row["first_name"].strip(),
                last_name=row["last_name"].strip(),
                grade=row["grade"].strip(),
            )
            for row in reader
        ]


def sort_by_last_name_desc(students: Iterable[Student]) -> List[Student]:
    """Return students sorted by last name descending (case-insensitive)."""

    return sorted(students, key=lambda student: student.last_name.lower(), reverse=True)


def format_student(student: Student) -> str:
    """Return a printable representation of a student."""

    return f"{student.last_name}, {student.first_name} — Grade {student.grade}"


def write_students(
    students: Iterable[Student],
    csv_path: Path,
) -> None:
    """Write *students* to *csv_path* in CSV format."""

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["first_name", "last_name", "grade"]
        )
        writer.writeheader()
        for student in students:
            writer.writerow(
                {
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "grade": student.grade,
                }
            )


if __name__ == "__main__":
    sorted_students = sort_by_last_name_desc(load_students())
    for student in sorted_students:
        print(format_student(student))

    write_students(sorted_students, DATA_PATH.with_name("students_sorted.csv"))
