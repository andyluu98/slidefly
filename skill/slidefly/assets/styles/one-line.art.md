# Vẽ một nét: luật vẽ minh họa SVG cho từng slide

Dùng cùng `one-line.css`. Cả deck là **một đường mực duy nhất** không nhấc bút: diễn viên `line` mang nét đó đi qua mọi slide, minh họa riêng của từng slide là những đoạn **một nét liền** nối vào hay nằm cạnh nét ấy. Deck mẫu: `gallery/78_demo-one-line.html`.

## 1. Tinh thần
- **Một nét liền trên giấy trắng ngà**, mực đen ấm. Mọi thứ là nét: nhân vật, đồ vật, cả thời gian. Không tô màu, không đổ bóng, không nền họa tiết, không viền kép.
- **Mỗi hình trong SVG là đúng một `<path>`** (hoặc một dãy path nối đầu nối đuôi). Nét có thể cắt chính nó và quay lại đường cũ; nhấc bút giữa chừng là sai luật.
- **Khoảng trắng là chất liệu chính**: 85 phần trăm khung phải là giấy trống. Thấy rối thì bỏ chi tiết, không thêm nét.
- **Đường nét của bàn tay**: dày khi chậm và rẽ gấp, mảnh khi chạy thẳng; run nhẹ ở đoạn dài. Hình hình học (nhà, máy bay) vẽ bằng đoạn thẳng có run 2 đến 3px, không bằng đường tròn hoàn hảo.
- **Một màu nhấn duy nhất, dùng đúng một lần** (đỏ `#C4372B` ở trái tim của slide kết, đã có trong diễn viên `line`). Minh họa riêng không dùng màu nhấn.
- Giấy luôn là nền của sân khấu; SVG không vẽ giấy, không vẽ khung, không vẽ lưới.
- Không phải bảng trắng (không bàn tay, không chữ dày đặc), không phải mực nước (không sắc độ), không phải hoạt họa nhiều nét rời.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (nét, chữ nhãn) | `#1D1A17` |
| Chữ phụ trong hình | `#6B645A` |
| Giấy (do nền sân khấu) | `#F8F5EE` |
| Màu nhấn, chỉ có trong `line` | `#C4372B` |

- Nét: `fill: none; stroke: #1D1A17; stroke-width: 3.4; stroke-linecap: round; stroke-linejoin: round`. Chỉ **một độ dày** trong mỗi hình; không nét mảnh phụ.
- Khai báo lớp `.ol-p` (nét), `.ol-lb` (nhãn), `.ol-sm` (nhãn phụ) trong `<style>` của deck để bản PPTX đọc được màu và nét.
- Vòng xoắn (loop) là phần thưởng của cây bút: dùng đường trochoid, `x = x0 + c t - r sin t`, `y = y0 - r (1 + cos t)`, t từ -π đến π, c khoảng 0,55 r; r từ 14 đến 26.
- Nơi bút dừng thì có **giọt mực**: một chấm đặc bán kính 6 đến 7px ở đầu nét đầu tiên.
- **Điểm bắt đầu và điểm dừng** của mỗi nét phải có chủ đích: bắt đầu ở giọt mực, dừng ở nơi nét gặp đường nền hoặc ở một vòng xoắn.
- **Tốc độ của bút** hiện qua hình dạng: đoạn dài thẳng là bút chạy nhanh, đoạn cong gấp và vòng xoắn là bút chậm.
- **Cắt chéo nét cũ** là hợp lệ và nên dùng ở chỗ hai cánh máy bay gặp nhau; không cần xóa hay che.
- Chữ trong SVG: `var(--font-hand)` (Patrick Hand), 28 đến 30px, mực; chỉ nhãn 1 đến 3 chữ. Chữ không bao giờ nằm trên nét.

## 3. Bộ hình mẫu lặp lại
**Nét vẽ dần** (mọi hình): `<path class="ol-p draw" pathLength="1" style="--d:.1" d="..."/>`; cần `morph-motion.css`.
**Vòng xoắn** trên đường nền:
```svg
<path class="ol-p" d="M20 90H100C130 90 150 60 138 52C124 44 116 70 134 82C152 94 170 90 200 90H260"/>
```
**Ngôi nhà một nét** (cửa trước rồi viền): cửa (30,0)(30,-34)(60,-34)(60,0), rồi (0,0)(0,-60)(45,-100)(90,-60)(90,0); nhân tỷ lệ và xoay để thành "tư thế" khác.
**Máy bay giấy**: mũi, cánh trên, khe lõm, cánh dưới, về mũi, nếp gấp, rồi đuôi kéo thành đường bay; tọa độ trong hộp 760x700: mũi (660,330), cánh trên (290,150), khe (430,335), cánh dưới (330,500).
**Cung nhảy** nối các trạm: `Q` lên cao 30 đến 35px giữa hai trạm.
**Vòng xoắn ốc** (cho mở phần, kết chương): bán kính giảm đều theo góc, 2 đến 2,5 vòng, khoảng cách giữa hai vòng 100 đến 130px; nét dừng ở tâm bằng một giọt mực. Đã có sẵn ở diễn viên `line` cho slide `section`, minh họa riêng không vẽ lại.
**Đường dẫn vào hình**: đoạn nét đi từ mép khung hay đường nền tới hình, tiếp tuyến với đường nền, không có góc gập ở chỗ nối; hình mới "mọc" ra từ đường cũ.
**Gập góc bằng tay**: cạnh thẳng vẽ bằng `Q` với điểm điều khiển lệch khỏi trung điểm 1 đến 3px (xem cách `wob()` trong deck mẫu), góc để nhọn, không bo.
**Hình tượng trưng gợi ý**: nhà (nơi bắt đầu), máy bay giấy (chuyển cảnh), vòng xoắn (thời gian), trái tim (lời cảm ơn), bậc thang (tăng trưởng); mỗi hình dưới 12 nét gập hoặc cong.
**Khoảng đệm**: giữ cách chữ tối thiểu 24px; nhãn 28 đến 30px cách nét 20px; hình không chạm vào mép an toàn 80px.
**Nhãn**: cụm ngắn, không khung, nằm dưới nét, cách nét tối thiểu 20px.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa bên trái (x 140 đến 1020). Hộp SVG `left:1100px; top:160px`, 760x700. Hình là một nét liền: giọt mực ở mũi, bao quanh máy bay, đuôi kéo xuống và **kết thúc đúng điểm (660,660) của hộp**, tức (1760, 820) trên sân khấu, nơi diễn viên `line` bắt đầu. Hai nét gặp nhau thành một. Không đặt gì khác trên x 1100 đến 1860, y 160 đến 860.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content`, x 1260 đến 1800, y 280 đến 980; chừa y 580 đến 680 cho `hl-text`. Nửa trên: cùng một vật hai tư thế (nhà nhỏ, nhà lớn nghiêng 10 độ) nối bằng một đường cong, nhãn "Tư thế A" và "Tư thế B" ngay dưới. Nửa dưới: một đường nền với ba vòng xoắn, mỗi vòng một thuộc tính (vị trí, cỡ, màu), nhãn bên dưới. Cùng một vật thì cùng nhãn.

**c. Quy trình hoặc dòng thời gian.** Diễn viên `line` đã là trục y 630 và đã có năm vòng nhỏ làm trạm (x = 136 + i x 342,4 trên sân khấu). SVG đặt `left:120px; top:560px`, cao 140: chỉ vẽ **chuỗi cung nhảy** `M16 70 Q187 4 358 70 Q529 4 700 70 ...` từ trạm này sang trạm kia, cao tối đa 35px trên trục (chữ bước lẻ kết thúc y 578). Ẩn chấm mặc định bằng `.timeline::before, .step::before { display: none; }` (đã có trong style).
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Slide `stats`, dải đáy y 836 đến 986: **một đường nền duy nhất** có số vòng xoắn bằng số ý: 3 vòng to dưới số đầu, 5 vòng vừa dưới số giữa, 7 vòng nhỏ dưới số cuối. Tâm cột: x 384, 960, 1536 (trong SVG: 264, 840, 1416). Không thêm số vào hình.

## 5. Chuyển động và xuất PPTX
- Nét tự vẽ ra: `draw` theo thứ tự cây bút đi; cả hình xong trong khoảng 2 giây. Nhãn bọc `<g class="reveal">` để hiện sau nét.
- Không animation lặp, không rung, không đổi màu. Giữa các slide, nét đường nền trượt (diễn viên `line` đổi tư thế) chứ không vẽ lại: đó là phép chuyển cảnh.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector, `draw` thành quét từ trái. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`. Chữ trong SVG không sửa được trong PowerPoint, nên chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Đếm `<path>`: mỗi hình một nét liền (ngoại lệ: giọt mực là `<circle>`); nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không phủ vùng `hl-text`.
- `deck.audit()` báo OK mọi slide; xuất thử `export-pptx.py` không lỗi.
- Rà màu: trong minh họa chỉ có mực `#1D1A17` và chữ phụ `#6B645A`.
- Rà nối: nếu hình chạm đường nền của sân khấu, điểm nối trùng đúng tọa độ trên sân khấu (cộng `left`, `top` của SVG), tiếp tuyến cùng hướng.
- Rà nhịp: thứ tự `draw` theo đúng đường đi của bút; `--d` tăng dần, không hai đoạn cùng lúc.
- Rà khoảng trắng: thu nhỏ slide về cỡ thumbnail, hình vẫn đọc được và vẫn còn ít nhất 80 phần trăm giấy trống.

## 6. Cấm
- Tô màu, đổ bóng, gradient, hạt nhiễu, viền kép, nền họa tiết trong hình.
- Màu nhấn trong minh họa riêng (màu nhấn chỉ dành cho trái tim ở diễn viên `line`).
- Nhấc bút: hai nét rời nhau không nối, hoặc nhiều hơn một giọt mực mỗi hình.
- Hình đè lên chữ của slide; hình lấp quá 15 phần trăm khung.
- Số đo, số liệu bịa trong hình; chữ dài trong SVG.
- Mũi tên có đầu tam giác đặc, hình học hoàn hảo (compa, thước), icon có sẵn; chúng phá cảm giác bàn tay.
- Cắt nét giữa chừng để "tẩy": bút không bao giờ tẩy, nét sai thì vẽ tiếp qua nó.
- Sao chép nhân vật, hình ảnh của một tác phẩm vẽ một nét có thật.

Phỏng theo lemo-opuscar `styles/one-line/STYLE.md` (MIT) qua MotionFly.
