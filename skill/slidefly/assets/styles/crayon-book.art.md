# Sách tranh sáp màu: luật vẽ minh họa SVG cho từng slide

Dùng cùng `crayon-book.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một trang truyện tranh thiếu nhi được tô bằng sáp màu. Deck mẫu: `gallery/76_demo-crayon-book.html`.

## 1. Tinh thần
- Cả deck là **một trang sách tranh** vẽ bằng sáp màu trên giấy có vân: nét sần, tô lem ra ngoài viền vài px, để hở những khe giấy trắng. Giọng kể dịu, chậm, như đọc truyện trước giờ ngủ.
- **Sáp chỉ bám vào đỉnh vân giấy**: vì vậy mọi mảng màu là các nét tô qua lại có khe hở, rải hạt giấy trắng lên trên, không bao giờ là mảng phẳng.
- **Logic của trẻ con**: nhà có một mặt tiền thẳng và một mặt hông nghiêng, người to hơn cửa, vật có mặt (mặt trời cười, ngôi sao có mắt, máy bay giấy). Vật được vẽ trước, màu tô sau.
- **Chừa giấy trắng**: sáp đậm màu trên nhiều giấy trống; độ đậm nhạt đến từ lực tay (gạch thưa hay dày), không thêm màu mới.
- **Mỗi hình kể một việc**: một vật chính, tối đa hai vật phụ, mọi thứ còn lại là màu nền của sân khấu.
- **Hộp khoảng 12 cây sáp, không hơn.** Viền luôn một màu chàm đậm, không dùng đen. Tối đa một mảng màu nước xanh, nó là khách, sáp mới là chủ.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Viền, mắt, nét chữ | `#2A2850` (`var(--ink)`) |
| San hô (mái, chữ nhấn) | `#D9543A`, tối hơn `#C94632` |
| Vàng nghệ (tường, sao) | `#F2B632`, viền sao `#E0961C` |
| Cam | `#EE8A2E` |
| Xanh lá (cỏ, tán cây) | `#5E9A4A` |
| Xanh da trời sáp | `#6F98D2` (cửa sổ `#7FB7E0`) |
| Hồng (má) | `#EE8FA0` |
| Nâu (thân cây, cửa) | `#8B5A3C` |
| Giấy, hạt trắng | `#F4EFE3` |
| Màu nước duy nhất | `#4C74D2`, độ đặc 0,1 đến 0,2 |

- Nét viền 4 đến 6px, kép: một nét đậm và một nét mảnh nửa độ dày, lệch nhẹ, `stroke-linecap` và `stroke-linejoin` là `round`. Chi tiết nhỏ (cửa sổ, quả táo) 3 đến 4px.
- **Mảng tô** = một đường `<path>` gồm nhiều đoạn `M x y Q x y x y` song song, cách nhau 6 đến 9px, `stroke-width` 6 đến 8, độ đặc 0,9, mỗi đoạn dài vượt mép 3 đến 6px. Vùng lớn thêm một lượt gạch chéo thưa độ đặc 0,4 với góc lệch khoảng 70 độ.
- **Vân giấy**: một `<pattern>` 96x96 các chấm màu giấy (`#F4EFE3`, bán kính 0,8 đến 1,4, độ đặc 0,7), dùng làm `fill` của một hình đa giác cùng đường bao với mảng tô, đặt ngay trên các nét tô. Id pattern là `tk`.
- Chữ trong SVG: `var(--font-display)` (Itim), 24 đến 26px, màu chàm; chỉ nhãn ngắn.
- Khai báo lớp chữ `.cy-lb`, `.cy-sm` trong `<style>` của deck để bản PPTX đọc được; màu nét và màu tô ghi thẳng bằng thuộc tính.

## 3. Bộ hình mẫu lặp lại
**Mảng tô sáp có vân** (hình bất kỳ, thay đa giác):
```svg
<defs><pattern id="tk" width="96" height="96" patternUnits="userSpaceOnUse"><path d="M12 20h.1M70 44h.1M40 80h.1" stroke="#F4EFE3" stroke-width="2.8" stroke-opacity=".72" stroke-linecap="round"/></pattern></defs>
<path d="M60 40Q120 36 180 44M178 52Q120 58 62 50M64 62Q120 66 176 60" stroke="#F2B632" stroke-width="7" stroke-opacity=".9" stroke-linecap="round" fill="none"/>
<path d="M56 36H184V120H56Z" fill="url(#tk)"/>
<path d="M56 36Q120 33 184 37Q187 80 184 120Q120 124 56 120Q53 80 56 36Z" stroke="#2A2850" stroke-width="5" stroke-linejoin="round" fill="none"/>
```
**Đường chấm sáp** (đường bay, mũi tên nối): nét `stroke-dasharray=".1 16"`, `stroke-width` 7 đến 8, đầu nét `round`, màu san hô; mũi tên là tam giác đặc nhỏ.
**Ngôi sao có mặt**: 5 cánh gập, tô vàng, viền cam đậm, hai chấm mắt chàm, nụ cười một nét cong, không quá 3 ngôi sao mỗi hình.
**Cây sáp** (hộp sáp để làm chú thích): thân chữ nhật có đầu nhọn, nhãn giấy trắng ở giữa với hai vạch màu, nhãn chữ bên phải.
**Chấm tròn tô sáp**: vòng tròn hơi méo, tô gạch chéo, viền chàm; dùng làm trạm, làm số lượng.
**Máy bay giấy**: ba mảnh tam giác chung một mũi (cánh trên vàng, cánh dưới san hô, nếp gấp đậm hơn), viền chàm vẽ dần; đường bay là một vòng xoắn chấm chấm phía sau đuôi.
**Số trong vòng tròn giấy**: vòng nền giấy, viền chàm 3,5px, số bằng `var(--font-display)`; cùng vật thì cùng số, đặt cạnh mỗi tư thế.
**Nhãn viết tay**: một cụm 2 đến 4 chữ cạnh hình (ví dụ "Tư thế A"), cỡ 24px màu `#5A5675`, không xuống dòng, không đặt trong khung.
**Vật có mặt**: hai chấm mắt chàm có chấm sáng giấy nhỏ, hai má hồng tô gạch, miệng một nét cong; chỉ cho vật chính của hình (mặt trời, ngôi sao), không cho mọi vật.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở trang trái (x 140 đến 1000). Trang phải đã có diễn viên: mảng nước, mặt trời, sao, nhà, cây, cỏ. Hình riêng của slide nằm trong khoảng trống giữa mặt trời và mái nhà: x 1150 đến 1810, y 290 đến 505. Deck mẫu: một chiếc máy bay giấy tô vàng và san hô bay ra khỏi vòng xoắn chấm chấm, có vài ngôi sao nhỏ.
- Lớp vẽ: đường bay chấm, hai cánh máy bay (tô trước, viền sau), nếp gấp, sao nhỏ. Không đè lên ống khói (cao nhất y 515) và mặt trời (thấp nhất y 290).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content`, x 1260 đến 1800, y 280 đến 980. Chừa dải y 580 đến 680 cho `hl-text`. Nửa trên: cùng một vật hai tư thế (bản mờ chấm chấm nhỏ, bản tô màu lớn nghiêng), nối bằng đường chấm có mũi tên, số trong vòng tròn giấy. Nửa dưới: hộp cây sáp, mỗi cây là một thuộc tính (vị trí, cỡ, màu).
- Cùng một vật thì cùng một số, đúng tinh thần Morph.

**c. Quy trình hoặc dòng thời gian.** SVG đặt `left:120px; top:560px`, cao 140, chồng lên trục y 630 (diễn viên `line` là nét sáp trục). Trạm thứ i của 5 cột: x = 16 + i x 342,4, y 70: một chấm tô sáp, mỗi trạm một màu theo thứ tự san hô, vàng, xanh lá, xanh da trời, hồng. Cung nối giữa hai trạm là đường chấm cao tối đa 30px trên trục (chữ bước lẻ kết thúc y 578), kèm mũi tên; trạm cuối thêm vòng san hô thứ hai. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Slide `stats`, dải đáy y 836 đến 986 dưới mỗi con số: số chấm tô sáp tỷ lệ với ý của số (deck mẫu: 3 chấm to, 5 chấm vừa, 7 chấm nhỏ, màu xoay vòng). Tâm cột: x 384, 960, 1536. Không thêm số mới vào hình.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường viền chính thêm `class="draw" pathLength="1" style="--d:.3"` (cần `morph-motion.css`); thứ tự: viền cánh trên, cánh dưới, nếp gấp. Không gắn `draw` vào nét chấm vì `draw` ghi đè `stroke-dasharray`.
- Cụm tô màu, số, nhãn: bọc `<g class="reveal">` để hiện sau nét.
- Không dùng animation lặp, không rung, không "sôi" nét (boil) vì bản PPTX không có.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành một hình vector, hiệu ứng `draw` thành quét từ trái. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`. Chữ trong SVG không sửa được trong PowerPoint, nên chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không phủ vùng `hl-text`.
- `deck.audit()` báo OK mọi slide; xuất thử `export-pptx.py` không lỗi.
- Rà màu: chỉ dùng các màu trong bảng; không quá một mảng màu nước mỗi slide; viền luôn chàm, không đen.

## 6. Cấm
- Mảng màu phẳng không có nét tô và vân, gradient mượt, bóng đổ, hiệu ứng thủy tinh, render 3D, filter làm mờ.
- Viền đen, hơn 12 màu sáp, hơn một màu nước, màu nước phủ lên nhân vật.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề.
- Số liệu bịa trong hình: chỉ dùng số lượng chấm khớp với số trong slide.
- Hình trẻ con có sẵn trong sách thật, nhân vật hay câu chữ của một cuốn sách có thật.

Phỏng theo lemo-opuscar `styles/crayon-book/STYLE.md` (MIT) qua MotionFly.
