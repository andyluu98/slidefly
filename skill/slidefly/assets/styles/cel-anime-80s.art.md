# Anime 80s: luật vẽ minh họa SVG cho từng slide

Dùng cùng `cel-anime-80s.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một cảnh cel của phim OVA cuối thập niên 80 phát lại trên băng video. Deck mẫu: `gallery/91_demo-cel-anime-80s.html`.

## 1. Tinh thần
- **Hai lớp tương phản làm nên diện mạo**: nền vẽ tay (gradient phun sơn, thành phố đêm, mặt trời vằn) ở lớp sân khấu; hình minh họa là **cel**: màu phẳng, ít màu, mỗi hình đúng **hai tông** (một mảng sáng, một mảng bóng cứng), không gradient trong hình.
- **Nét viền có màu, không bao giờ đen tuyền**: viền là bản đậm của màu tô (`var(--ink)` #1d0f3d cho vật thể, hồng, cyan hay vàng cho nét neon). Vật cứng như tivi, băng cassette được phép viền ink đậm.
- **Ánh sáng sau lưng**: biển hiệu, màn hình, đèn LED phát sáng xuyên qua hình. Vẽ bằng một nét đậm sáng chồng lên nét to hơn, mờ (độ mờ 0,2 đến 0,3), không dùng `filter`.
- **Đồ vật thời đó là nhân vật**: tivi CRT, băng VHS, cassette, bộ đèn equalizer, biển neon, vệt đèn xe. Không vẽ người, không vẽ nhân vật hay xe, mecha, tên, logo của một phim có thật. Chữ trên biển là ký hiệu chung.
- **Điều khiển ánh sáng thay vì vẽ lại**: một dải sáng quét qua hình giữ nguyên là đủ chuyển động.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Nét vật thể, đồng tử | `var(--ink)` #1d0f3d, lớp `.an-o` dày 5, `.an-m` 3,5, `.an-s` 2,5 |
| Thân vật (tivi) | `#5a3a9c` (`.g-body`), bóng cứng `#3b2575` (`.g-bodyd`), viền sáng cyan |
| Màn hình, nền tối | `#13093a` (`.g-scr`); bảng menu `rgba(12,5,40,.8)` viền cyan |
| Kem, giấy | `#fff0d9` (`.g-cream`) |
| Neon hồng | `#ff4fa3` (`.g-pink`), vàng `#ffc857` (`.g-gold`), cyan `#5ee7ff` (`.g-cyan`), tím `#7a3fd1` |
| Cel trong suốt | hồng, cyan, vàng với độ mờ 0,14 đến 0,18, nét 3,5 cùng màu (`.an-c1 .an-c2 .an-c3`) |
| Quầng sáng | cùng màu neon, độ mờ 0,10 đến 0,2 (`.g-halo`) |

- Hai tông: tô màu chính, rồi **một** mảng bóng cứng (đa giác hay cung, tông đậm hơn một bậc, đặt phía xa nguồn sáng), rồi một nét sáng mảnh ở mép gần nguồn sáng. Không bóng mềm.
- Viết màu bằng lớp CSS khai báo trong `<style>` của deck (tiền tố `an-`, `g-`), không viết `fill="var(...)"` trong thuộc tính: trình xuất PPTX chỉ đổi biến khi màu nằm trong lớp.
- Chữ trong hình: nhãn OSD của đầu băng dùng `var(--font-display)` (Barlow Condensed nghiêng, 700), kem hoặc cyan, 26 đến 40px. Câu cần sửa để ngoài SVG.

## 3. Bộ hình mẫu lặp lại
**Tivi CRT** (bìa): thân bo góc, màn hình bo cong, hai núm, khe loa, chân, râu ăng ten có bi vàng, viền sáng cyan ở mép trên. Màn hình chiếu một slide thu nhỏ.
```svg
<rect class="an-o g-body" x="140" y="170" width="400" height="304" rx="36"/>
<path class="g-bodyd" d="M540 206V438Q540 474 504 474H300Q470 450 540 206Z"/>
<path class="an-rim draw" pathLength="1" d="M156 214Q156 186 184 184H500"/>
```
**Băng cassette**: chữ nhật bo góc ink, nhãn hồng, hai ổ cuộn tròn. Đặt nghiêng -13 độ, đè lên góc dưới của vật chính.
**Cel trong suốt** (sơ đồ khái niệm): hình bình hành `M20 0H230L210 140H0Z`, tô màu mờ, viền cùng màu; ba tấm xếp chéo như bộ cel nhiều lớp (multiplane), mỗi tấm một bóng số hồng và một ký hiệu bên trong.
**Menu OSD của đầu băng**: khung tối bo góc viền cyan, dòng `MENU` và `CH 04` ở góc, dòng chọn có nền hồng 50%, ba dòng lệnh kèm tam giác `&#9654;`.
**Trạm neon** (mốc thời gian): vòng ink viền cyan 6, chấm trắng giữa, quầng cyan r 40; trạm cuối viền hồng, quầng hồng lớn hơn, thêm sao.
**Bộ LED equalizer** (số liệu): khung tối viền cyan, mỗi cột là chồng đoạn LED cao 8, cách 2,6 px, từ dưới lên: cyan, vàng, hồng; chấm trắng giữ đỉnh ở trên mỗi cột.
```svg
<circle class="g-halo2" cx="358" cy="70" r="40"/>
<circle class="an-st" cx="358" cy="70" r="24"/><circle class="g-white" cx="358" cy="70" r="9"/>
<rect class="g-cyan" x="12" y="134" width="40" height="8" rx="2"/><rect class="g-gold" x="12" y="82" width="40" height="8" rx="2"/>
```
**Vật chọn theo chủ đề**: ánh sáng và màn hình nói "chiếu, hiển thị"; băng, cassette nói "lưu, quay lại"; equalizer nói "mức độ, tải"; biển neon nói "địa điểm, thương hiệu"; xe và đường nói "tiến độ", nhưng chỉ vẽ vệt đèn, không vẽ xe có thật.
**Sao lóe bốn cánh** (`star4`) cho điểm sáng; **vệt sáng** là nền (diễn viên `streak`) nên hình không tự vẽ lại.

## 4. Bốn công thức
Khung 1920x1080, SVG đặt bằng `style="left:..px; top:..px"` kèm `width`, `height`, `viewBox`.

**a. Bìa.** Chữ bìa nằm trái (x 120 đến 1040, style đã đặt). Hình nằm trong x 1120 đến 1820, y 200 đến 740, trùng mặt trời của diễn viên `sun` (tâm 1500, 520). Tivi ở giữa sao cho mặt trời ló ra sau thân; râu ăng ten, băng cassette ở góc trái dưới, sao lóe ở góc phải trên, nhãn `&#9654; PLAY` và bộ đếm băng ở góc trái trên. Màn hình chiếu đúng chủ đề (ở deck mẫu là một slide).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980), chừa dải y 600 đến 660 cho `hl-text`. Nửa trên: các thành phần là các tấm cel xếp chéo từ thấp bên trái lên cao bên phải, nối nhau bằng mũi tên chấm hồng, mỗi tấm một bóng số. Nửa dưới: bảng menu OSD với đúng ngần ấy dòng, dòng đầu được chọn.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline` (SVG top 560, cao 140, trục ở y 70); diễn viên `streak` đã là trục ánh sáng. Mỗi bước một trạm neon ở x = 136 + i x 342,4 (5 bước, bước cuối viền hồng và có sao), tam giác chỉ hướng ở giữa hai trạm, đường dóng chấm lên xuống 44px. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dải đáy y 836 đến 986, tâm cột x 384, 960, 1536: mỗi cột một bộ equalizer rộng 236px. Số cột LED bằng số ý (3, 5, 7), độ cao và độ dày kể đúng ý của con số (ít ý thì cột thấp, to; nhiều ý thì cột cao, mảnh, chạm vùng hồng, thêm đèn báo quá tải màu đỏ).

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1" style="--d:.2"` (cần `morph-motion.css`). Không gắn `draw` vào nét đứt hay chấm vì `draw` ghi đè `stroke-dasharray`.
- Hiện: bọc `<g class="reveal">` cho nhãn, sao, menu. **Không đặt `reveal` hay `animation` lên phần tử đã có thuộc tính `transform`**: CSS thay mất phép dời; bọc thêm một `<g transform>` bên ngoài.
- Dải sáng quét một lần khi slide đến: `.slide.active .an-sweep` chạy `anSweep` 1,6s (mờ dần vào, trượt 180px, mờ dần ra). Không có animation lặp. Có `@media (prefers-reduced-motion: reduce)` tắt.
- Nhịp gợi ý: viền chính `--d:0`, chi tiết `--d:.2`, nhãn và sao hiện sau bằng `reveal`; cả hình xong trong khoảng 2 giây.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left; top"` và `width`, `height` thì thành một hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp. Animation `anSweep` không sang PowerPoint.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.

## 6. Kiểm trước khi giao
- Nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không lấn vùng chữ của bước timeline.
- `deck.audit()` mọi slide `OK`; xuất thử `export-pptx.py` không lỗi.
- Chữ trong SVG đủ tương phản (kem hoặc cyan trên nền tối); khung tối của menu luôn có nền đặc 80%.

## 7. Cấm
- Nhân vật, xe, mecha, địa danh, tên, logo, cảnh nổi tiếng của một phim có thật; nhân vật mắt tròn khổng lồ kiểu hiện đại, mặt đỏ má gạch.
- Nét đen tuyền đều tăm tắp, gradient trong hình, `filter` blur, `mix-blend-mode`, ảnh bitmap nhúng.
- Hiệu ứng gate weave hay vết xước phim: đây là băng video, không phải phim nhựa.
- Đè hình lên chữ; số liệu bịa trên các thanh (dùng cột ký hiệu, hoặc nhãn "VÍ DỤ").
- Hình quá đông: mỗi slide một vật chính, phần còn lại là sao và quầng sáng.
- Hai vật chính tranh nhau cùng một vùng sáng; màu neon thứ tư ngoài hồng, cyan, vàng (trừ đèn báo đỏ ở slide quá tải).
- Hình che mất mặt trời hoặc vệt sáng của sân khấu khi chúng đang là điểm nhấn của layout đó.

Phỏng theo lemo-opuscar `styles/cel-anime-80s/STYLE.md` (MIT) qua MotionFly.
