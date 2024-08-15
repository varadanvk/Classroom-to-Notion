import json
import os
from typing import List, Dict, Any

class NotionAssignmentMatcher:
    def __init__(self, activities: List[Dict[str, Any]], output_path: str):
        self.activities = activities
        self.output_path = output_path

    def assign_teachers(self) -> None:
        print("Assign teachers to activities:")
        for activity in self.activities:
            teacher = input(f"Enter teacher name for '{activity['title']}' (or press Enter to skip): ")
            activity['teacher'] = teacher.strip()

    def save_activities(self) -> None:
        with open(self.output_path, 'w') as file:
            json.dump(self.activities, file, indent=2)
        print(f"Activities with teachers saved to {self.output_path}")

    def match_assignment_to_activity(self, assignment: Dict) -> str:
        posted_by = assignment.get('posted_by', '').lower()
        for activity in self.activities:
            if activity['teacher'].lower() in posted_by:
                return activity['id']
        return ''

    def run(self) -> None:
        if not self.activities:
            print("No activities provided.")
            return

        self.assign_teachers()
        self.save_activities()

        print("\nMatching system ready. You can now use this to match assignments to activities.")

    def get_activities(self) -> List[Dict]:
        return self.activities