# Hoạt hình viễn tưởng: luật vẽ minh họa SVG cho từng slide

Dùng cùng `scifi-toon.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một cảnh trong phim hoạt hình sitcom khoa học viễn tưởng dành cho người lớn. Deck mẫu: `gallery/90_demo-scifi-toon.html`.

## 1. Tinh thần
- **Phim hoạt hình 2D truyền hình**: nét viền dày đồng đều màu tím đen, màu phẳng, mỗi hình chỉ một mảng bóng đổ cứng. Không gradient trong hình, không 3D, không phối cảnh.
- **Đồ khoa học viễn tưởng được đối xử như đồ gia dụng**: đĩa bay, hành tinh, cổng không gian, điều khiển từ xa. Chuyện nhỏ làm bằng phương tiện khổng lồ, và nhân vật phản ứng bằng cặp mắt trắng to, đồng tử bé tí.
- **Nhân vật là thứ của deck**: một slide có mắt, miệng, tay chân sợi mì (xem công thức bìa). Tự bịa nhân vật, đạo cụ, thiết bị cổng. Không vẽ nhân vật, hình bóng, tổ hợp màu hay logo của phim có thật.
- **Mỗi layout là một thế giới màu mới** (lớp sân khấu đổi `--bg`). Hình vẽ phải đọc được trên mọi nền, nên viền ink luôn là thứ giữ hình.
- **Chỉ cổng không gian được phát sáng.** Màu tím hồng của cổng không dùng cho vật nào khác.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Viền và mắt, đồng tử | `var(--ink)` (#2a1d3a), lớp `.st-o` dày 6, `.st-m` 4,5, `.st-s` 3,5 |
| Giấy, thân slide, sao | `#fff6c9` (`.f-cream`) |
| Vàng đất, viền cửa sổ, thân đĩa | `#f4b942` (`.f-pop`), bóng `#d98d1e` |
| Hồng da, người ngoài hành tinh | `#f4a3c4` (`.f-pink`) |
| Kính, giọt mồ hôi | `#bfe9f2` (`.f-sky`) |
| Tím đồ vật (chân đĩa, điều khiển) | `#8f6bb3` (`.f-vio`) |
| San hô, giày, hành tinh | `#ef8a6b` (`.f-cor`) |
| Xanh bạc hà, vòng hành tinh, chữ terminal | `#7ad3c4` (`.f-teal`) |
| Cổng: viền, lòng, tay xoáy, lõi | `#b25cff`, `#5a1fb0`, `#efd3ff`, `#fff3ff` |
| Bóng đổ cứng | `.f-shade` (mực 20%), chỉ một mảng, đặt ở phía xa nguồn sáng |

- **Chất liệu**: `stroke-linejoin` và `stroke-linecap` luôn `round`. Tay chân là nét sợi mì `.st-leg` dày 9, đầu tay là bàn tay găng trắng tròn, bàn chân là elip san hô.
- **Mắt**: tròn trắng viền ink, đồng tử đen 8 đến 10px nhìn lệch lên một bên, lông mày là một cung ink. Miệng mở có mảng nâu mận `.f-mouth` và lưỡi hồng.
- Viết màu bằng lớp CSS khai báo trong `<style>` của deck (xem deck mẫu), không viết `fill="var(...)"` trong thuộc tính: trình xuất PPTX chỉ đổi biến khi màu nằm trong lớp.
- Chữ: nhãn ngắn dùng `var(--font-display)` (Baloo 2 đậm); dòng lệnh terminal dùng `var(--font-mono)` (VT323) màu bạc hà trên khối ink. Tiếng Việt có dấu dùng cả hai font đều ổn.

## 3. Bộ hình mẫu lặp lại
**Đĩa bay** (240x140, hàm `saucer(cx, cy, scale, rot)` trong deck mẫu): chân tím, vòm kính sky, người ngoài hành tinh hồng với hai mắt tròn, thân vàng elip, mảng bóng đáy, năm đèn kem. Dùng cho "một vật đang di chuyển", "người làm", "dịch vụ".
```svg
<ellipse class="st-o f-pop" cx="120" cy="80" rx="112" ry="32"/>
<path class="f-popd" d="M12 88A108 30 0 0 0 228 88A108 20 0 0 1 12 88Z"/>
<ellipse class="st-d" cx="120" cy="80" rx="112" ry="32" style="stroke-width:6"/>
```
**Cổng không gian** (`portal_mini`): viền gợn bằng đường cong mượt, lòng tím đậm, ba tay xoáy ngắn màu nhạt, lõi sáng. Là "trạm", "bước chuyển", "nơi đến".
**Slide có mặt**: cửa sổ kem bo góc, thanh tiêu đề vàng với hai chấm, hai mắt to, một miệng. Số dòng chữ giả (nét `.st-bar`) cho biết nội dung nhiều hay ít.
```svg
<rect class="st-o f-cream" x="190" y="190" width="300" height="200" rx="22"/>
<circle class="st-o st-m f-white" cx="268" cy="276" r="38"/><circle class="f-ink" cx="278" cy="266" r="9"/>
<path class="st-d" d="M226 232Q262 210 298 228"/>
```
**Bốn nét biểu cảm** (đổi mặt là đổi nghĩa): mắt trợn miệng mở nghĩa là bất ngờ, mặt cười nhỏ là ổn, vạch miệng phẳng là trung tính, mày cong và giọt mồ hôi là quá tải.
**Hành tinh có vành**, **mặt trăng có miệng hố**, **sao bốn cánh** (`star4`): chấm phá nền, mỗi hình một mảng bóng cứng.
**Thẻ terminal**: chữ nhật ink bo góc, dòng `&gt; ...` màu bạc hà, con trỏ là khối chữ nhật. Dùng làm tiêu đề hình hoặc bảng kê.
**Đường bay**: chấm tròn xếp thưa `st-dot` (`stroke-dasharray: 0.1 13` kèm đầu tròn) kết thúc bằng mũi tên ink đặc.

## 4. Bốn công thức
Khung 1920x1080, SVG đặt bằng `style="left:..px; top:..px"` và có đủ `width`, `height`, `viewBox`.

**a. Bìa.** Chữ bìa nằm trái (x 120 đến 1040, style đã đặt). Hình nằm trong x 1120 đến 1820, y 200 đến 740, tâm hình trùng tâm diễn viên `portal` (1440, 520). Một slide nhân vật nhảy ra khỏi cổng: thân kem nghiêng -8 độ, tay phải giơ điều khiển từ xa, chân sợi mì đạp trong cổng, vài vạch tốc độ phía trên, sao bốn cánh quanh. Góc trái trên là thẻ terminal `&gt; TÊN_`. Vật nhảy ra là ẩn dụ của chủ đề.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980). Chừa dải y 600 đến 660 cho `hl-text`. Nửa trên: cùng một vật ở hai tư thế (bản mờ nhỏ và bản đậm lớn nghiêng) nối bằng đường bay chấm, cùng số trong bong bóng kem nghĩa là cùng một vật. Nửa dưới: bảng terminal ink với ba dòng lệnh ngắn và con trỏ.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline` (SVG top 560, cao 140, trục ở y 70). Mỗi bước một cổng nhỏ (rx 30, ry 38) ở x = 136 + i x 342,4 (5 bước), trạm cuối là hành tinh có vành. Giữa hai trạm là đường bay chấm cao tối đa 32px trên trục và đầu mũi tên; một đĩa bay nhỏ nhảy giữa trạm 3 và 4. Ẩn trục và chấm mặc định: `.s-tl .step::before, .s-tl .timeline::before { display: none; }`. Không vẽ vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dải đáy y 836 đến 986: mỗi cột một slide có mặt rộng 200px, tâm x 384, 960, 1536. Ít ý thì dòng giả dày và mặt cười; nhiều ý thì dòng mỏng dần, mặt phẳng rồi mặt toát mồ hôi. Cột cuối bị xé đôi bằng đường zigzag và thẻ `TÁCH!`. Hai phương án thì vẽ hai hình cùng cỡ cạnh nhau.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1" style="--d:.2"` (cần `morph-motion.css`), dùng cho tay chân và viền. Không gắn `draw` vào nét chấm vì `draw` ghi đè `stroke-dasharray`.
- Hiện: bọc `<g class="reveal">` cho nhãn, sao, bảng. **Không đặt `class="reveal"` hay `animation` lên phần tử đã có thuộc tính `transform`**: CSS thay mất phép dời. Bọc thêm một `<g transform="...">` bên ngoài.
- Nhịp gợi ý: viền chính `--d:0`, tay chân `--d:.1` đến `.2`, nhãn và sao hiện sau bằng `reveal`; cả hình xong trong khoảng 2 giây để người nói không phải chờ.
- Một lần nảy khi slide đến: `.slide.active .st-pop` chạy `stPop` 0,9s (bóp từ `scale(.55, .4)` về nguyên, `transform-origin: 50% 80%`), như vật vừa đáp xuống. Không có animation lặp, không rung nét. Có `@media (prefers-reduced-motion: reduce)` tắt.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left; top"` và `width`, `height` thì thành một hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp, nên mọi lớp đặt tiền tố `st-` hoặc `f-`. Animation `stPop` không sang PowerPoint.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình: chỉ để nhãn ngắn (thẻ terminal, số). Câu cần sửa để ngoài SVG.

## 6. Kiểm trước khi giao
- Nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không lấn vùng chữ của bước timeline.
- `deck.audit()` mọi slide `OK`; xuất thử `export-pptx.py` không lỗi.
- Rà màu: trong SVG chỉ có các lớp ở bảng màu; cổng là thứ duy nhất tím sáng.

## 7. Cấm
- Nhân vật, hình bóng, tổ hợp màu, tên, câu cửa miệng, logo, khẩu súng cổng của bất kỳ phim có thật nào. Gu chung (sitcom viễn tưởng người lớn) thì được, bản sao thì không.
- Gradient trong hình, bóng đổ mờ, render 3D, hiệu ứng glow ngoài cổng, `filter` blur.
- Bộ ba xanh chanh chói, giọt nhầy chảy và chữ bong bóng lượn sóng đi cùng nhau (đọc ra một chương trình cụ thể).
- Đè hình lên chữ; nét chạy qua hàng tiêu đề; số liệu bịa (dùng chữ ký hiệu hoặc "VÍ DỤ").
- Hình quá đông: mỗi slide một nhân vật chính, phần còn lại là chấm phá.
- Màu ngoài bảng ở mục 2, và dùng màu tím sáng của cổng cho thứ không phải cổng.

Phỏng theo lemo-opuscar `styles/scifi-toon/STYLE.md` (MIT) qua MotionFly.
