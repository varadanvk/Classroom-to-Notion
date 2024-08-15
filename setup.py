from services.matcher import NotionAssignmentMatcher
from scripts.load_activities import load_activities
import json

try:
    loaded_activities = load_activities()
    print(f"Loaded activities type: {type(loaded_activities)}")
    print(f"Number of activities loaded: {len(loaded_activities)}")
    print("First few activities:")
    print(json.dumps(loaded_activities[:5], indent=2))

    matcher = NotionAssignmentMatcher(activities=loaded_activities, output_path="constants/activities_with_teachers.json")
    matcher.run()
except Exception as e:
    print(f"An error occurred: {str(e)}")
    import traceback
    traceback.print_exc()