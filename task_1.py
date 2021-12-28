import argparse
import json
import xml.etree.cElementTree as ET


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("rooms", type=str, help="This will be name of input rooms file")
    parser.add_argument(
        "students", type=str, help="This will be name of input students file"
    )
    parser.add_argument(
        "st_in_rooms", type=str, help="This will be name of output result file"
    )
    return parser.parse_args()


class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def __repr__(self):
        return f"<Student {self.id} {self.name}>"


class Room:
    def __init__(self, room_id, name, students):
        self.id = room_id
        self.name = name
        self.students = students

    def __repr__(self):
        return f"<Room {self.id} {self.name} {self.students}>"


def bl(data_about_rooms, data_about_students):
    students_by_room = {}
    for el in data_about_rooms:
        key = el["id"]
        students_by_room[key] = []

    for evidence_of_student in data_about_students:
        room = evidence_of_student["room"]
        student = Student(evidence_of_student["id"], evidence_of_student["name"])
        students_by_room[room].append(student)

    students_in_rooms = []
    for evidence_of_room in data_about_rooms:
        room_id = evidence_of_room["id"]
        room = Room(
            evidence_of_room["id"], evidence_of_room["name"], students_by_room[room_id]
        )
        students_in_rooms.append(room)
    return students_in_rooms


def json_serializer(args):
    with open(args.rooms, "r") as rooms_file:
        data_about_rooms = json.load(rooms_file)
    with open(args.students, "r") as students_file:
        data_about_students = json.load(students_file)

    students_in_rooms = bl(data_about_rooms, data_about_students)

    result = []
    for room in students_in_rooms:
        student_dicts = [dict(id=s.id, name=s.name) for s in room.students]
        item = {
            "id": room.id,
            "name": room.name,
            "students": student_dicts,
        }
        result.append(item)

    with open(args.st_in_rooms, "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def xml_serializer(args):
    students_xml_tree = ET.parse(args.students)

    root = students_xml_tree.getroot()
    data_about_students = [child.attrib for child in root]

    rooms_xml_tree = ET.parse(args.rooms)

    root = rooms_xml_tree.getroot()
    data_about_rooms = [child.attrib for child in root]

    students_by_room = bl(data_about_rooms, data_about_students)

    root = ET.Element("xml")
    for r in students_by_room:
        room = ET.SubElement(root, "room", attrib={"id": r.id, "name": r.name})
        for st in r.students:
            student = ET.SubElement(
                room, "student", attrib={"id": st.id, "name": st.name}
            )

        tree = ET.ElementTree(root)
        tree.write(args.st_in_rooms)


def main(args):
    if (
        args.students.endswith(".json")
        and args.rooms.endswith(".json")
        and args.st_in_rooms.endswith(".json")
    ):
        json_serializer(args)

    if (
        args.students.endswith(".xml")
        and args.rooms.endswith(".xml")
        and args.st_in_rooms.endswith(".xml")
    ):
        xml_serializer(args)


if __name__ == "__main__":
    args = parse_args()
    main(args)
