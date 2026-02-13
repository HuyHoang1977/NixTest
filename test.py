import re

def count_telex():
    while True:
        #Nhập dữ liệu
        user_input = input("Nhập chuỗi latin: ").strip()
        if not user_input:
            print("Chuỗi không được để trống.")
            continue
        #Kiểm tra ký tự đặc biệt/khoảng trắng
        if not re.match(r"^[a-zA-Z0-9]+$", user_input):
            print(f"Chuỗi chứa khoảng trắng hay ký tự đặc biệt.")
            continue
        #Nếu dữ liệu đúng, tiến hành đếm
        matches = re.findall(r"aw|aa|dd|ee|oo|ow|w", user_input.lower())
        
        print(f"Output: {len(matches)} ({', '.join(matches)})")
        break

if __name__ == "__main__":
    count_telex()