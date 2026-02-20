# ==========================================
# TASK ENGINE TEST
# ==========================================

from runtime.task.task_engine import TaskEngine

print("\n[TEST] Task Engine Phase\n")

engine = TaskEngine()

print(engine.execute("GET_TIME", ""))
print(engine.execute("SET_WATER_REMINDER", ""))
print(engine.execute("TAKE_NOTE", "नोट लिखो यह टेस्ट नोट है"))
print(engine.execute("READ_NOTES", ""))