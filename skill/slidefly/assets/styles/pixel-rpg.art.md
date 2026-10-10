# Pixel RPG: luật vẽ minh họa SVG cho từng slide

Dùng cùng `pixel-rpg.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một khung hình chụp từ trò chơi nhập vai 16-bit. Deck mẫu: `gallery/86_demo-pixel-rpg.html`.

## 1. Tinh thần
- Cả deck là **một màn hình game nhập vai**: bản đồ ô gạch cuộn từng ô, cửa sổ hộp thoại viền vát, thanh HP, rương và nhân vật 16 x 16 đi dọc mép cửa sổ. Hình minh họa là **ảnh chụp màn hình của chính trò chơi đó**.
- **Chữ là hộp thoại và bảng lệnh**: nhãn ngắn, IN HOA cho tên mục, chữ thường cho ghi chú. Câu dài để ngoài SVG.
- **Mọi thứ nằm trên lưới pixel.** Không đường cong thật, không nét mảnh hơn một ô, không xoay chéo tùy ý (xoay chỉ theo bội 90 độ). Chiều sâu chỉ bằng bóng ô và viền vát.
- Câu chuyện nhỏ cho mỗi hình: đi tới, gặp, mở rương, chọn lệnh. Nhân vật chính (áo xanh, khăn đỏ) luôn là cùng một người.
- **Ngôn ngữ của hệ thống game:** bản đồ, bảng lệnh, túi đồ, thanh trạng thái, hộp thoại. Chọn đúng một hệ thống cho mỗi hình, đừng trộn ba hệ thống trong một khung.
- Cảnh sáng, tươi bên trong cửa sổ (cỏ xanh, đường cát) tương phản với chrome UI tối bên ngoài: hình luôn nằm trong một cửa sổ có khung, không trôi tự do trên nền.

## 2. Bảng màu, nét, chất liệu
Bảng màu có chỉ số, khoảng 20 màu, tên theo vai trò:
| Vai trò | Giá trị |
|---|---|
| Mực, viền mọi vật | #1a1c2c |
| Cửa sổ, nền bảng | #29366f (xanh), #3a2a5e (tím), viền sáng #94b0c2, viền tối #1b2350 |
| Chữ, điểm sáng | #f4f4f4, vàng #ffcd75, cam #ef7d57 |
| Cỏ, lá | #38b764, sáng #a7f070, tối #1f7a46, #257179 |
| Đất, đá, gỗ | #f2c27a (đường), #c98f4e (mép), #7d93a8 (đá tường), #8b5a2f (gỗ) |
| Nhấn | đỏ #b13e53, xanh dương #3b5dc9, trời #41a6f6, cyan #73eff7, tím #5d275d |

- **Ô lưới 8px** (hoặc 4px cho chi tiết). Mọi `<rect>` có tọa độ và kích thước là bội của 4. Bọc nhóm pixel bằng `shape-rendering="crispEdges"`.
- **Viền một ô quanh mọi vật.** Bóng đổ là một dải cùng tông tối, không mờ. Vòng tròn vẽ bằng từng hàng pixel (đĩa pixel), không dùng `<circle>`.
- **Cửa sổ vát:** viền mực ngoài, vạch sáng ở trên và trái, vạch tối ở dưới và phải, ruột phẳng:
```svg
<rect x="0" y="0" width="520" height="250" fill="#1a1c2c"/><rect x="6" y="6" width="508" height="238" fill="#29366f"/>
<rect x="6" y="6" width="508" height="4" fill="#94b0c2"/><rect x="6" y="6" width="4" height="238" fill="#94b0c2"/>
<rect x="6" y="240" width="508" height="4" fill="#1b2350"/><rect x="510" y="6" width="4" height="238" fill="#1b2350"/>
```
- Chữ: `var(--font-display)` (VT323), nhãn 32 đến 40px. Khai báo lớp trong `<style>` của deck (`.pr-t .pr-m .pr-n .pr-i`) để bản PPTX đọc được.

## 3. Hình mẫu lặp lại
**Sprite 16 x 16** viết bằng chữ, mỗi ký tự một ô (`.` là trống), vẽ ở 5 đến 6px một ô:
```
.....kkkkkk.....   k = mực    h = tóc    s = da
....khhhhhhk....   r = khăn   b = áo     y = đai
...kskssssksk...   B = quần   n = giày
```
Bộ sprite có sẵn: người hùng, rương, quái nhầy (xanh lá, mắt hai ô). Ba nhân vật này lặp ở mọi hình; thêm nhân vật mới chỉ khi nội dung cần.
**Đĩa pixel** cho đồng xu, huy hiệu, bóng số: bán kính 2 đến 4 ô, viền mực, điểm sáng một ô lệch trên trái.
**Cây:** hai đĩa xanh chồng (tối rồi sáng) trên thân nâu hai ô. **Lâu đài:** tường đá, một hàng lỗ châu mai, hai tháp mái đỏ, cổng tối có ổ khóa vàng.
**Con đường:** các khúc chữ nhật vuông góc màu cát, viền mép #c98f4e lớn hơn 6px mỗi phía.
**Dấu hỏi, dấu chấm than:** hình vuông vàng một ô với nét mực, đặt trên đầu quái.
**Thanh HP:** các ô 15 x 18px, ô đầy màu xanh lá có vạch sáng ở trên, ô rỗng #333c57.
**Biển chỉ đường:** cột gỗ hai ô, tấm biển chữ nhật vát viền, một nhãn tên mục ngắn (VT323 32px) và một mũi tên ba ô.
**Hộp thoại có chân dung:** cửa sổ vát, bên trái ô vuông 64px chứa mặt nhân vật (hai ô mắt, một ô miệng), bên phải một hai dòng chữ; góc dưới phải một mũi tên ▼ vàng.
**Chỉ dùng thêm sprite** khi nội dung đòi hỏi: biển, ngọn đuốc, cổng, bình thuốc. Mỗi sprite thêm vào phải vẽ cùng lưới 16 x 16, cùng viền mực một ô.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm trong cửa sổ bên trái (x 80 đến 1080). Hình đặt trong x 1120 đến 1820, y 200 đến 740, là **một cửa sổ bản đồ** (khung vát, thanh tiêu đề "BẢN ĐỒ · CHƯƠNG 1", ruột là bản đồ ô gạch nhìn từ trên). Lớp vẽ: nền cỏ, hoa cỏ, đường dẫn tới lâu đài, cây, lâu đài, rồi nhân vật, quái, rương. Dưới hình, diễn viên `road` (y 912) có hàng nhân vật đi cùng.
- Vật của chủ đề thành một địa điểm: lâu đài là đích, đường là quy trình, rương là kết quả.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Trong cửa sổ tím của diễn viên `panel` (x 1240 đến 1820, y 250 đến 1010). Chừa dải y 600 đến 660 cho `hl-text` (SVG y 320 đến 380). Nửa trên: nhân vật ở hai tư thế (đứng, nhảy lên có tia sáng) nối bằng cung nhảy các ô vàng, bóng số giống nhau cho cùng một vật, nhãn "TƯ THẾ A" và "TƯ THẾ B" trên nền sàn. Nửa dưới: **bảng lệnh** (cửa sổ vát) mỗi hàng một ô số, tên lệnh bên trái, ghi chú bên phải, hàng đầu được chọn (nền xanh sáng).

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên con đường y 630 của `timeline`. Mỗi bước một "trạm" là đĩa pixel (đường kính 72px) có biểu tượng: cuộn giấy, sao, búa, kính lúp; trạm cuối là rương nằm trên đường. Giữa các trạm là dấu chân (ô vuông vàng 12px, so le hai hàng). Trạm ở x = 136 + i × 342,4 làm tròn theo 8px. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ vào vùng chữ (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986: mỗi cột một ô túi đồ (cửa sổ vát 260 x 108) chứa đúng bấy nhiêu đồng xu bằng số ý (3 to, 5 vừa, 7 nhỏ); cột "nên tách slide" thêm huy hiệu đỏ có dấu chấm than. Tâm cột: x 384, 960, 1536.

## 5. Chuyển động và xuất PPTX
- Hiện theo nhịp "bật" từng nhóm: `<g class="reveal-scale">` cho sprite và cửa sổ, `reveal` cho nhãn; thêm `style="--i:n"` để so le. Đặt `.art .reveal-scale { transform-box: fill-box; transform-origin: 50% 80%; }` trong `<style>` của deck.
- Không đặt `transform` trên chính phần tử có lớp `reveal*`; bọc thêm một `<g>` ngoài.
- Không animation lặp, không mờ dần: sprite xuất hiện tức thì theo bậc, không nội suy màu.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Chỉ dùng `<rect>`, `<text>`, `<g>`; không `<circle>` hay `<path>` cong để bản vector giữ nguyên độ vuông. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: pixel không bị mờ, nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ dùng bảng ở mục 2; mọi vật có viền mực.

## 6. Cấm
- Làm mờ, gradient mịn, bóng đổ mờ, chuyển màu giữa hai ô, render 3D, hiệu ứng CRT hay đường quét.
- Tên, nhân vật, khung giao diện, phông chữ, logo, giai điệu của trò chơi nhập vai có thật; nhân vật người thật.
- Số HP, số điểm bịa: dùng thanh đầy hoặc ô số chỉ thứ tự (1, 2, 3).
- Đè hình lên chữ của slide; câu dài trong SVG.
- Pha pixel kích cỡ khác nhau trong cùng một hình (sprite 5px cạnh nền 8px là được, nhưng không dùng 3px hay 7px).
- Ảnh chụp bitmap hay `<image>` nhúng: mọi pixel phải là một `<rect>`.

Phỏng theo lemo-opuscar `styles/pixel-rpg/STYLE.md` (MIT) qua MotionFly.
