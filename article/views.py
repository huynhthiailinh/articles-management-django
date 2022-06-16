from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Trung tâm Học liệu và Truyền thông, Trường Đại học Bách khoa, ĐHĐN',
        'title': 'DUT tổ chức thành công kỳ thi Olympic Cơ học toàn quốc lần thứ XXXII năm 2022- cụm Miền Trung',
        'content': 'Sáng ngày 12/06/2022, Kỳ thi Olympic Cơ học toàn quốc lần thứ XXXII năm 2022- cụm Miền Trung đã được diễn ra tại Trường Đại học Bách khoa, ĐHĐN. Cuộc thi thực sự là sân chơi khoa học trí tuệ của những người trẻ đam mê khoa học cơ bản, đam mê Cơ học.',
        'date_posted': '14/06/2022 10:53',
    },
    {
        'author': 'Trung tâm Học liệu và Truyền thông, Trường Đại học Bách khoa, ĐHĐN',
        'title': 'NCS Trần Thị Ngọc Thư bảo vệ thành công Luận án Tiến sĩ cấp Trường chuyên ngành Công nghệ thực phẩm',
        'content': 'Sáng ngày 04/6/2022, Trường Đại học Bách khoa - Đại học Đà Nẵng đã tổ chức buổi bảo vệ Luận án Tiến sĩ cấp Trường của Nghiên cứu sinh (NCS) Trần Thị Ngọc Thư, chuyên ngành Công nghệ thực phẩm, với đề tài: “Nghiên cứu xây dựng quy trình công nghệ thu nhận isoflavone từ một số nguồn thực vật và ứng dụng sản xuất thực phẩm chức năng”. Đề tài dưới sự hướng dẫn của PGS.TS. Trương Thị Minh Hạnh – Trường Đại học Bách khoa, ĐHĐN và TS. Bùi Xuân Vững – Trường Đại học Sư phạm, ĐHĐN.',
        'date_posted': '14/06/2022 10:11',
    },
    {
        'author': 'Quang Phong',
        'title': 'Lễ ký kết thỏa thuận hợp tác (MoU) giữa Khoa Điện, Trường Đại học Bách Khoa, ĐHĐN và Công ty Trace Software International France (TSI)',
        'content': 'Chiều ngày 09/06/2022, tại phòng khách khu A, Trường Đại học Bách Khoa - Đại học Đà Nẵng đã diễn ra Lễ ký kết thỏa thuận hợp tác (MOU) giữa Công ty Trace Software International (TSI) với Khoa Điện, Trường Đại học Bách khoa - Đại học Đà Nẵng. TSI là công ty dẫn đầu toàn cầu trong việc phát triển các giải pháp phần mềm và dịch vụ tư vấn cho kỹ thuật công nghiệp, với chuyên môn độc đáo trong việc thiết kế lắp đặt điện trong sản xuất, năng lượng, tòa nhà, y tế, nhà máy ....TSI hiện diện tại hơn 50 quốc gia trên toàn thế giới thông qua các nhà phân phối và đối tác được ủy quyền.',
        'date_posted': '13/06/2022 15:45',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'article/home.html', context)

def about(request):
    return render(request, 'article/about.html', {'title':'About'})
