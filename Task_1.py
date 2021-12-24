import argparse
import json
import xml.etree.cElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('rooms', type=str, help='This will be name of input rooms file')
parser.add_argument('students', type=str, help='This will be name of input students file')
parser.add_argument('st_in_rooms', type=str, help='This will be name of output result file')
args = parser.parse_args()


class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name


class Room:
    def __init__(self, room_id, name, students):
        self.id = room_id
        self.name = name
        self.students = students


def bl(data_about_students, data_about_rooms):
    rooms_for_students = {key: [] for key in range(len(data_about_rooms))}
    for evidence_of_student in data_about_students:
        room = evidence_of_student["room"]
        student = Student(evidence_of_student["id"], evidence_of_student["name"])
        rooms_for_students[room].append(student)

    students_in_rooms = []
    for evidence_of_room in data_about_rooms:
        room_id = evidence_of_room["id"]
        room = Room(evidence_of_room["id"], evidence_of_room["name"], rooms_for_students[room_id])
        students_in_rooms.append(room)
    return students_in_rooms


def json_serializer():
    with open(args.rooms, "r") as rooms_file:
        data_about_rooms = json.load(rooms_file)
        print(data_about_rooms)
    with open(args.students, "r") as students_file:
        data_about_students = json.load(students_file)

    students_in_rooms = bl(data_about_rooms, data_about_students)

    result = [{}, {}]
    for room in students_in_rooms:
        item = {
            "id": room.id,
        }
        result.append(item)

    with open(args.st_in_rooms, "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


# def xml_serializer():
#     students_xml_tree = ET.parse("students.xml")
#     """
#     <xml>
#       <student id=12312 name="gratest mind ever" room=105 />
#       ....
#     </xml>
#     """
#     data_about_students = [child.attrib for child in students_xml_tree]
#
#     rooms_xml_tree = ET.parse("rooms.xml")
#     """
#     <xml>
#       <room id=12312 name="gratest mind ever" />
#       ....
#     </xml>
#     """
#     data_about_rooms = []
#     for child in rooms_xml_tree:
#         data_about_rooms.append(child.attrib)
#
#     students_by_room = bl(data_about_students, data_about_rooms)
#
#     rooms = ET.Element("rooms")
#     room = ET.SubElement(rooms, "room")
#     ET.SubElement(room, "room_id")
#     ET.SubElement(room, "room_name")
#     students = ET.SubElement(room, "students")
#     ET.SubElement(students, "student_id")
#     ET.SubElement(students, "student_name")
#
#     tree = ET.ElementTree(rooms)
#     tree.write("filename.xml")

#
#
# while True:
#     user_answer = input("Choose output file's type: json(1) or xml(2)")
#     try:
#         user_answer = int(user_answer)
#     except ValueError:
#         continue
#     else:
#         if user_answer == 1 or user_answer == 2:
#             break
#         else:
#             continue
#
# if user_answer == 1:
#     json_serializer()
# else:
#     xml_serializer()

json_serializer()
