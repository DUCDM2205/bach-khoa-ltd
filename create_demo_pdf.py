from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "documents" / "ho-so-nang-luc-demo.pdf"

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))

blue = colors.HexColor("#114A91")
navy = colors.HexColor("#082B59")
amber = colors.HexColor("#F59E0B")
pale = colors.HexColor("#EDF5FC")
styles = getSampleStyleSheet()
title = ParagraphStyle("TitleVN", fontName="Arial-Bold", fontSize=27, leading=32, textColor=navy, alignment=TA_CENTER, spaceAfter=12)
h1 = ParagraphStyle("H1VN", fontName="Arial-Bold", fontSize=20, leading=25, textColor=navy, spaceAfter=12)
h2 = ParagraphStyle("H2VN", fontName="Arial-Bold", fontSize=13, leading=17, textColor=blue, spaceBefore=8, spaceAfter=7)
body = ParagraphStyle("BodyVN", fontName="Arial", fontSize=10.5, leading=16, textColor=colors.HexColor("#25364a"), spaceAfter=9)
badge = ParagraphStyle("Badge", fontName="Arial-Bold", fontSize=10, textColor=colors.HexColor("#241b04"), alignment=TA_CENTER)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(navy)
    canvas.rect(0, A4[1] - 16 * mm, A4[0], 16 * mm, fill=1, stroke=0)
    canvas.setFont("Arial-Bold", 9)
    canvas.setFillColor(colors.white)
    canvas.drawString(18 * mm, A4[1] - 10 * mm, "BÁCH KHOA LTD · HỒ SƠ DEMO")
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawString(18 * mm, 12 * mm, "Dữ liệu minh họa - Không dùng làm hồ sơ dự thầu hoặc chứng minh năng lực")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Trang {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm, topMargin=28 * mm, bottomMargin=22 * mm)
story = [Spacer(1, 25 * mm), Paragraph("HỒ SƠ NĂNG LỰC", title), Paragraph("CÔNG TY TNHH XÂY DỰNG ĐIỆN BÁCH KHOA", title), Spacer(1, 8 * mm)]
label = Table([[Paragraph("DỮ LIỆU MINH HỌA · BẢN DUYỆT GIAO DIỆN", badge)]], colWidths=[135 * mm])
label.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), amber), ("BOX", (0, 0), (-1, -1), 0, amber), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
story += [label, Spacer(1, 15 * mm), Paragraph("Vững kỹ thuật - Bền công trình", ParagraphStyle("Slogan", parent=body, fontName="Arial-Bold", fontSize=16, alignment=TA_CENTER, textColor=blue)), Spacer(1, 45 * mm), Paragraph("Tài liệu này chỉ dùng để kiểm tra thao tác xem/tải PDF và duyệt bố cục. Mọi số liệu, dự án, chứng chỉ và thông tin liên hệ cần được thay bằng dữ liệu đã xác thực trước khi công bố.", ParagraphStyle("Note", parent=body, alignment=TA_CENTER, fontSize=11))]
story += [PageBreak(), Paragraph("01 · Tổng quan", h1), Paragraph("Bách Khoa LTD định hướng cung cấp giải pháp xây dựng điện cho chủ đầu tư, nhà thầu và các đơn vị công nghiệp. Nội dung dưới đây mô phỏng cấu trúc hồ sơ chính thức và chưa phải tuyên bố năng lực thực tế.", body), Paragraph("Lĩnh vực hoạt động", h2)]
services = [["01", "Hệ thống điện công nghiệp"], ["02", "Điện năng lượng mặt trời"], ["03", "Bảo trì hệ thống điện"], ["04", "Trạm biến áp và đường dây"], ["05", "Thiết kế và tư vấn"], ["06", "Hệ thống M&E / MEP"], ["07", "Điện dân dụng"]]
t = Table(services, colWidths=[18 * mm, 135 * mm], rowHeights=10 * mm)
t.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "Arial"), ("FONTNAME", (0, 0), (0, -1), "Arial-Bold"), ("TEXTCOLOR", (0, 0), (0, -1), colors.white), ("BACKGROUND", (0, 0), (0, -1), blue), ("BACKGROUND", (1, 0), (1, -1), pale), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("GRID", (0, 0), (-1, -1), .5, colors.white)]))
story += [t, Spacer(1, 8 * mm), Paragraph("Năng lực minh họa", h2), Paragraph("Nhân sự: Đang cập nhật · Thiết bị: Đang cập nhật · Chứng chỉ: Đang cập nhật · Dự án tiêu biểu: Dữ liệu minh họa", body)]
story += [PageBreak(), Paragraph("02 · Quy trình dự án", h1), Paragraph("Một luồng làm việc rõ ràng giúp các bên thống nhất phạm vi, chất lượng, tiến độ và hồ sơ bàn giao.", body)]
steps = [["01", "Khảo sát & yêu cầu", "Ghi nhận hiện trạng, phụ tải và ràng buộc vận hành."], ["02", "Thiết kế & đề xuất", "Lập phương án kỹ thuật, khối lượng và tiến độ."], ["03", "Thi công & kiểm soát", "Tổ chức thi công, an toàn và kiểm soát chất lượng."], ["04", "Đo kiểm & bàn giao", "Thí nghiệm, nghiệm thu và hướng dẫn vận hành."]]
t2 = Table(steps, colWidths=[14 * mm, 48 * mm, 92 * mm], rowHeights=20 * mm)
t2.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "Arial"), ("FONTNAME", (0, 0), (1, -1), "Arial-Bold"), ("TEXTCOLOR", (0, 0), (0, -1), amber), ("BACKGROUND", (0, 0), (-1, -1), pale), ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#c8d7e6")), ("INNERGRID", (0, 0), (-1, -1), .5, colors.white), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
story += [t2, Spacer(1, 12 * mm), Paragraph("Thông tin cần bổ sung trước công bố", h2), Paragraph("Logo chính thức, địa chỉ, hotline, email, hồ sơ pháp lý, số liệu nhân sự - thiết bị, danh sách dự án được phép công khai, chứng chỉ còn hiệu lực và hình ảnh có quyền sử dụng.", body), Spacer(1, 15 * mm), Paragraph("BACH KHOA CONSTRUCTION ELECTRICITY COMPANY LIMITED", ParagraphStyle("End", parent=body, fontName="Arial-Bold", fontSize=14, alignment=TA_CENTER, textColor=navy))]
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUTPUT)
