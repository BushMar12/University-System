from model.database import Database

class AdminController:
    def __init__(self):
        try:
            self.students = Database.load_data()
        except Exception as e:
            print(f"[ERROR] Failed to load student data: {e}")
            self.students = []

    def clear_database(self):
        try:
            Database.clear_data()
            self.students = []
        except Exception as e:
            print(f"[ERROR] Failed to clear the database: {e}")

    def list_students(self):
        return self.students

    def group_students(self):
        groups = {"HD": [], "D": [], "C": [], "P": [], "F": []}
        for student in self.students:
            try:
                grade = student.get_grade_group()
                if grade in groups:
                    groups[grade].append(student)
                else:
                    print(f"[WARNING] Unknown grade group for student ID {student.id}: {grade}")
            except Exception as e:
                print(f"[ERROR] Failed to group student ID {getattr(student, 'id', 'Unknown')}: {e}")
        return groups

    def partition_students(self):
        partition = {"PASS": [], "FAIL": []}
        for student in self.students:
            try:
                average = student.calculate_average()
                if average >= 50:
                    partition["PASS"].append(student)
                else:
                    partition["FAIL"].append(student)
            except Exception as e:
                print(f"[ERROR] Failed to calculate average for student ID {getattr(student, 'id', 'Unknown')}: {e}")
        return partition

    def remove_student(self, student_id):
        student_id = str(student_id)
        found = False
        updated_students = []

        try:
            for student in self.students:
                if student.id != student_id:
                    updated_students.append(student)
                else:
                    found = True

            if found:
                self.students = updated_students
                try:
                    Database.save_data(self.students)
                except Exception as e:
                    print(f"[ERROR] Failed to save data after removing student: {e}")
                    return False
                return True
            else:
                print(f"[INFO] Student ID {student_id} not found.")
                return False
        except Exception as e:
            print(f"[ERROR] Exception occurred during student removal: {e}")
            return False

