from abc import ABC

class Person:
    def __init__(self, name, age):
        self._name = name          
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Tuổi không hợp lệ!")

class Student(Person):
    def __init__(self, name, age, student_id, classroom):
        super().__init__(name, age)
        self.__student_id = student_id    # Thuộc tính private
        self.__classroom = classroom

    def get_student_id(self):
        return self.__student_id

    def get_classroom(self):
        return self.__classroom

    def set_classroom(self, classroom):
        self.__classroom = classroom

    def display_info(self):
        print(f"ID: {self.__student_id}, Họ tên: {self._name}, Tuổi: {self._age}, Lớp: {self.__classroom}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(" Thêm học sinh thành công!")

    def update_student(self, student_id, name=None, age=None, classroom=None):
        for student in self.students:
            if student.get_student_id() == student_id:
                if name:
                    student.set_name(name)
                if age:
                    student.set_age(age)
                if classroom:
                    student.set_classroom(classroom)
                print(" Cập nhật thông tin thành công!")
                return
        print(" Không tìm thấy học sinh!")

    def delete_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                print(" Đã xóa học sinh!")
                return
        print("Không tìm thấy học sinh!")

    def display_all(self):
        if not self.students:
            print("Danh sách học sinh trống!")
        else:
            print("\n Danh sách học sinh:")
            for student in self.students:
                student.display_info()

def menu():
    manager = StudentManager()

    while True:
        print("\n====== MENU QUẢN LÝ HỌC SINH ======")
        print("1. Thêm học sinh")
        print("2. Cập nhật thông tin học sinh")
        print("3. Xóa học sinh")
        print("4. Hiển thị tất cả học sinh")
        print("5. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            name = input("Nhập tên học sinh: ")
            age = int(input("Nhập tuổi: "))
            student_id = input("Nhập mã học sinh: ")
            classroom = input("Nhập lớp: ")
            student = Student(name, age, student_id, classroom)
            manager.add_student(student)

        elif choice == "2":
            student_id = input("Nhập mã học sinh cần cập nhật: ")
            name = input("Nhập tên mới (Enter nếu bỏ qua): ")
            age_input = input("Nhập tuổi mới (Enter nếu bỏ qua): ")
            classroom = input("Nhập lớp mới (Enter nếu bỏ qua): ")

            age = int(age_input) if age_input else None
            manager.update_student(student_id, name if name else None, age, classroom if classroom else None)

        elif choice == "3":
            student_id = input("Nhập mã học sinh cần xóa: ")
            manager.delete_student(student_id)

        elif choice == "4":
            manager.display_all()

        elif choice == "5":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    menu()
