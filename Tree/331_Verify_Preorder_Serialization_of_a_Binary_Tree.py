class JudgeSerialization:
    def is_valid_serialization(self, preorder: str) -> bool:
        preorder_list = preorder.split(",")
        slot = 1
        for element in preorder_list:
            if not slot:
                return False

            if element.isdigit():
                slot += 1
            
            else:
                slot -= 1
            
        return slot == 0


if __name__ == "__main__":
    print(JudgeSerialization().is_valid_serialization("1,2,#,#,#"))