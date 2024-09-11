# sử dụng selenium để crawl mã số thuế từ trang https://masothue.com/
# sử dụng multiprocessing để crawl nhanh hơn
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# sử dụng firefox
from selenium.webdriver.firefox.options import Options

# Cấu hình tùy chọn cho Firefox
firefox_options = Options()
# firefox_options.add_argument('--headless')  # Chạy Firefox ở chế độ không có giao diện
firefox_options.add_argument('--no-sandbox')  # Cần thiết khi chạy trong Docker
firefox_options.add_argument('--disable-dev-shm-usage')  # Giảm thiểu vấn đề về bộ nhớ
# Khởi tạo trình duyệt Firefox với các tùy chọn đã cấu hình
driver = webdriver.Firefox(options=firefox_options)

# lưu tab hiện tại:
main_tab = driver.current_window_handle
# tạo một vòng lặp từ 1 đến 10
for i in range(10):
    # mở link sau: https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/ho-chi-minh-23?page=i
    driver.get(f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/ho-chi-minh-23?page={i+1}')
    # tìm thẻ div class = 'tax-listing', sử dụng By.CLASS_NAME, tìm các thẻ div có class là 'tax-listing'
    tax_list_div = driver.find_element(By.CLASS_NAME, 'tax-listing')
    # lấy các thẻ div con cấp 1 của thẻ div tax_list_div
    tax_list = tax_list_div.find_elements(By.CSS_SELECTOR, ':scope > div')
    # duyệt qua các thẻ div con
    for tax in tax_list:
        # tạo một mảng để lưu thông tin mã số thuế
        tax_infos = []
        # lấy thuộc tính href của thẻ a
        a = tax.find_element(By.TAG_NAME, 'a')
        href = a.get_attribute('href')
        # mở tab mới
        driver.execute_script("window.open('');")
        # chuyển qua tab mới
        driver.switch_to.window(driver.window_handles[-1])
        # mở link
        driver.get(href)
        # tìm thẻ table có class là 'table-taxinfo'
        table = driver.find_element(By.CLASS_NAME, 'table-taxinfo')
        # lấy nội dung text trong thẻ thead
        thead = table.find_element(By.TAG_NAME, 'thead').text
        # thêm thead vào mảng tax_infos
        tax_infos.append(thead)
        # lấy thẻ tbody
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        # lấy các thẻ tr trong tbody
        trs = tbody.find_elements(By.TAG_NAME, 'tr')
        # duyêt qua các thẻ tr
        for tr in trs:
            # lấy các thẻ td trong tr
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if tds[0].text == 'Mã số thuế':
                # thêm thông tin mã số thuế vào mảng tax_infos
                tax_infos.append(tds[1].text.strip())
            if tds[0].text == 'Địa chỉ':
                # thêm thông tin địa chỉ vào mảng tax_infos
                tax_infos.append(tds[1].text.strip())
            if tds[0].text == 'Điện thoại':
                # thêm thông tin điện thoại vào mảng tax_infos
                tax_infos.append(tds[1].text.strip())
        print(tax_infos)
        # mở file data.csv ở chế độ ghi thêm, uft-8
        f = open('data.csv', 'a', encoding='utf-8')
        try:
            # lần lượt ghi thông tin trong mảng tax_infos vào file data.csv
            f.write(','.join(tax_infos) + '\n')
        finally:
            # đóng file lại
            f.close()
        # đóng tab hiện tại
        driver.close()
        # quay lại tab chính
        driver.switch_to.window(main_tab)

