import os

# Đường dẫn đến thư mục chứa các tệp HTML
project_path = r"c:\xampp\htdocs\htnq\information"

# Đoạn mã cần thêm
font_awesome_link = '''    <!-- Adding Font Awesome for icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">'''

navbar_code = '''    <!-- Navbar with home icon and link to dashboard -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'dashboard' %}">
          <i class="fas fa-home"></i> Trang Chủ
        </a>
      </div>
    </nav>'''

# Hàm để thêm đoạn mã vào tệp HTML
def update_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Thêm Font Awesome vào phần <head>
                if font_awesome_link not in content:
                    content = content.replace(
                        "</head>",
                        f"{font_awesome_link}\n</head>"
                    )

                # Thêm Navbar vào phần <body>
                if navbar_code not in content:
                    content = content.replace(
                        "<body",
                        f"<body>\n{navbar_code}\n"
                    )

                # Ghi lại nội dung đã chỉnh sửa vào tệp
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

# Chạy hàm cập nhật
update_html_files(project_path)
print("Đã cập nhật tất cả các tệp HTML trong thư mục 'information/templates'!")