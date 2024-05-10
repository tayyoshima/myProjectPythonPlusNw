while True:
    try:
        x = int(input("Input A:"))
        y = int(input("Input B: "))
        print(x/y)
    except ZeroDivisionError:
        print("ตัวแปร y ไม่สามารถหารด้วย 0 กรุณาระบุเลขใหม่ให้ถูกต้องครับ")
    except ValueError:
        print("ข้อมูลเข้าต้องเป็นตัวเลข")
    except Exception as e:
        print(e)
    finally:
        print("ขอบคุณที่ใช้บริการ")