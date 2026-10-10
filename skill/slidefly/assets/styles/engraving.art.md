# Tranh khắc đồng: luật vẽ minh họa SVG cho từng slide

Dùng cùng `engraving.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một "HÌNH n" trên cùng một tờ in khắc đồng. Deck mẫu: `gallery/70_demo-engraving.html`.

## 1. Tinh thần
- Cả deck là **một tờ in từ bản đồng** trên giấy kem có vân: mực một màu nâu đen, đóng khung như tờ minh họa sách khoa học thế kỷ 19 (chủ thể đặt giữa, bóng số, chú thích chữ nghiêng).
- **Độ đậm nhạt chỉ làm bằng nét, không bao giờ tô mảng.** Chỗ sáng là giấy trắng; nửa tối là một họ nét song song; bóng đổ là họ nét thứ hai cắt chéo; chỗ tối nhất thêm họ thứ ba.
- **Mỗi nét phình ra rồi thon lại** như nét đục: mảnh ở đầu, dày ở giữa, nhọn ở cuối. Nét một độ dày từ đầu đến cuối trông như bút vẽ vector, cấm.
- **Màu đến sau, bằng tay:** chỉ một lớp màu nước trong (hổ phách), lem ra ngoài nét một chút, mực luôn nằm trên. Một deck dùng tối đa một sắc phụ là đỏ nâu (`--rose`) cho nhãn chữ, không đưa vào hình.
- Khác `vintage-editorial` (báo ảnh kem với chữ lớn) và `paper-ink` (chữ in mực trên giấy): ở đây hình là nét khắc đan chéo, có khung in và bóng số.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (nét, chữ) | `var(--ink)` (#1c1510) |
| Nét mảnh, đường dẫn | `var(--line-soft)` (mực 60%) |
| Giấy, quầng quanh chủ thể | `var(--paper)` (#f1e8d2); tờ giấy rời `var(--paper-2)` |
| Nước màu hổ phách | `var(--wash)` (#c98a2e), `fill-opacity` 0,4 |
| Nhãn chữ đỏ nâu (ngoài hình) | `var(--rose)` |

- Họ nét ghi theo độ dày lớn nhất trên khung 1920x1080: đường bao 3 đến 4px, họ thứ nhất 2 đến 2,6px, họ chéo 1,7 đến 2,1px, họ thứ ba 1,5px, nét mảnh 1,3px. Khoảng cách giữa các nét tính theo hình, khoảng 1/60 chiều cao hình (5 đến 8px), họ sau thưa hơn họ trước một chút để hình nhỏ không bị xám.
- **Nét là hình, không là `stroke`:** mỗi nét là một đa giác hình thoi dài (xem mục 3), tô `var(--ink)`. Cả họ nét gom vào một `<path class="eg-ink">`. Chỉ vòng tròn nhỏ, đường dẫn và nét mảnh dùng `stroke`.
- Cắt mỗi đường dài thành các đoạn 70 đến 190px, mỗi đoạn tự phình tự thon, hai đoạn kề nhau chồng nhẹ: đúng cách tay thợ nhấc đục lên.
- Ánh sáng một hướng cho cả deck: **từ trên trái**. Mép tối ở dưới phải; đường bao dày hơn ở phía xa nguồn sáng.
- **Che khuất theo thứ tự vẽ:** quầng giấy (`.eg-halo`) rồi lớp màu, rồi nét tô bóng, rồi đường bao. Quầng giấy bao quanh chủ thể 12 đến 16px để nền kẻ dòng của vòng tròn không chạm vào nét.
- Chữ: nhãn là chữ hoa kiểu `var(--font-display)` (Playfair Display SC 700, giãn 0,1em); chú thích và số là chữ nghiêng `var(--font-body)` (Newsreader). Nhãn 19 đến 24px.
- Khai báo lớp trong `<style>` của deck (`.eg-ink .eg-o .eg-h .eg-halo .eg-wash .eg-stip .eg-tab .eg-ring .eg-num .eg-lb .eg-it`, xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Bộ hình mẫu lặp lại
**Một nét đục** (hình thoi dài, rộng nhất ở giữa; độ rộng nửa nét = w/2 x sin(pi u)^0,7, lấy 7 điểm mỗi bên):
```svg
<path class="eg-ink" d="M10 100L40 99L70 98.2L100 97.9L130 98.2L160 99L190 100L160 101L130 101.8L100 102.1L70 101.8L40 101Z"/>
```
**Họ nét theo hình:** nét chạy theo chiều của mặt (cánh nghiêng thì nét song song mép cánh), bắt đầu từ chỗ tối rồi thưa dần về phía sáng. Vùng sáng nhất để trống.
**Nét chéo** chỉ xuất hiện ở nửa tối: họ hai lệch họ một 50 đến 70 độ, họ ba chỉ ở khe sâu.
**Bóng số** (vòng tròn giấy, số chữ nghiêng, đường dẫn mảnh kết thúc bằng chấm):
```svg
<path class="eg-h" d="M552 330L592 262"/><circle class="eg-dot" cx="552" cy="330" r="3.2"/>
<circle class="eg-ring" cx="600" cy="248" r="17"/><text class="eg-num" x="600" y="255" text-anchor="middle">1</text>
```
**Quả cầu khắc** (chấm tối nhất ở dưới phải, một họ nét ở nửa tối, họ chéo ở bóng đổ; dùng làm "trạm", "điểm nhấn"): vẽ vòng `eg-o` rồi các nét theo `tone = 1 - n.l`.
**Nước màu lem:** chính đa giác của vật, dịch (+5, +4) rồi tô `.eg-wash`, vẽ trước các nét để mực nằm trên.
**Vòng kính lúp (roundel):** diễn viên `roundel` đã có nền kẻ dòng và hai vòng; minh họa vẽ chủ thể giữa vòng, bọc quầng giấy. Hình phóng to đặt trong `roundel2`, nối bằng diễn viên `leader`.
**Nhãn hình:** `HÌNH n · TÊN` chữ hoa kèm một gạch chân mảnh, dưới là một dòng chữ nghiêng nói rõ hình đang xem.

**Dựng nhanh bằng script** (khi hình cần hàng trăm nét): viết một hàm nhỏ ở thư mục nháp, không để trong skill.
- `lens(p0, p1, w)`: chia đoạn thành 7 điểm, mỗi điểm lệch hai bên vuông góc một đoạn w/2 x sin(pi u)^0,7, nối thành đa giác.
- `hatch(vùng, tone, góc, bước, ngưỡng)`: kẻ các đường song song, cắt theo vùng lồi, chỗ nào `tone` vượt ngưỡng thì cắt thành đoạn 70 đến 190px, mỗi đoạn một `lens` có độ rộng tăng theo `tone`.
- `tone(x, y)`: số từ 0 đến 1, tính từ khoảng cách tới nếp gấp (cánh), tới mép tối (hộp), hoặc `1 - n.l` (quả cầu). Ghi số lẻ một chữ số thập phân để SVG gọn.
- In ra một `<path class="eg-ink" d="...">` cho mỗi họ nét rồi dán vào deck; kiểm lại bằng cách mở ảnh chụp, không đo bằng mắt trên mã.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở bên trái (x 120 đến 1040). Hình nằm trong vòng `roundel` (tâm 1470, 480, bán kính 350) và đè lên vết nước màu của `wash`; SVG đặt tại left 1120, top 130, rộng 700, cao 880 để chứa cả `roundel2` (tâm 1250, 880, bán kính 100) ở góc dưới.
- Lớp vẽ: dấu vệt bay bằng chấm (stipple), quầng giấy, màu nước, họ nét tô bóng, đường bao đục từng đoạn, bóng số 1; chú thích dưới vòng. Hình 2 là cùng vật phóng to một chi tiết, cắt gọn trong vòng nhỏ (không tràn mép).
**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Trên slide `content`, đặt trong tờ giấy rời `slip` (x 1240 đến 1820, y 262 đến 992), tức vùng điểm nhấn x 1260 đến 1800. Chừa dải y 560 đến 680 cho `hl-text`. Nửa trên: vật ở hai tư thế (tư thế cũ vẽ mờ, một họ nét, tư thế mới dày và tô bóng) nối bằng một cung tên phình thon. Nửa dưới: bảng kê khung đôi, mỗi hàng một số trong vòng, tên chữ nghiêng, mẫu nét (một, hai, ba họ).
**c. Quy trình hoặc dòng thời gian.** SVG chồng lên trục y 630 của `timeline` (left 120, top 560, cao 140), tự vẽ trục bằng hai nét thon (dày và mảnh) kèm mũi tên. Trạm ở x = 136 + i x 342,4: năm quả cầu **khắc dần** (chỉ viền, một họ nét, nét chéo, nét tối, thêm màu nước), đúng ba lượt khắc của thợ. Cung nối cao tối đa 30px trên trục. Ẩn chấm mặc định: `.step::before { display: none; }` đã có trong style.
**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải y 836 đến 986, mỗi cột một khung đôi 220x110 tâm tại x 384, 960, 1536. Trong khung là các nét ngang phình thon thay cho dòng chữ: càng nhiều ý, càng nhiều nét và nét càng mảnh. Dưới khung một chữ nghiêng 20px ("thoáng", "vừa", "dày"). Vết nước `wash` của style đã nằm sau con số giữa.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"` (cần `morph-motion.css`); chỉ dùng cho nét có `stroke` (cung, đường dẫn). Các họ nét là hình tô nên cho hiện bằng `<g class="reveal">`, không vẽ dần.
- Thứ tự gợi ý: quầng và màu trước, họ nét một, họ nét chéo, đường bao, rồi nhãn và bóng số. Cả hình xong trong khoảng 2 giây.
- Không đặt thuộc tính `transform` trực tiếp lên phần tử có lớp `reveal` (CSS của lớp này ghi đè và mất vị trí): bọc thêm một `<g transform>` bên trong.
- Không dùng animation lặp, không rung, không đổi màu. Màu nước chỉ hiện một lần cùng cả hình.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì thành một hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.eg-ink`), nên giữ tiền tố `eg-`. Dùng `<g transform="translate() rotate()">` được; không dùng `clipPath` cho hình lớn (cắt sẵn đa giác bằng tính toán).
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được: chỉ để nhãn ngắn, câu cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, vòng kính lúp không đè bullet.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ có `var(--ink)`, `var(--line-soft)`, `var(--paper)`, `var(--paper-2)`, `var(--wash)`.
- Phóng to một góc: mọi nét phải thon hai đầu; nếu thấy nét đều như bút thì làm lại.

## 6. Cấm
- Tô mảng xám hoặc đen đặc (chỉ được dày nét), gradient, bóng đổ mờ, render 3D, hiệu ứng ánh kim hay glow.
- Màu nước đục, màu nước phủ lên chữ, đường kẻ hay giấy ngoài chủ thể; quá một sắc nước trong cùng slide.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề.
- Ghi số đo hay số liệu bịa trong hình: chỉ dùng số bóng (1, 2, 3), tên hình và chữ ngắn.
- Sao chép một tờ minh họa có thật, khung, tên hay chữ ký của người khắc; chép lại bố cục của deck mẫu cho đề tài khác.
- Nét một độ dày từ đầu đến cuối, nét đều như vẽ máy.

Phỏng theo lemo-opuscar `styles/engraving/STYLE.md` (MIT) qua MotionFly.
