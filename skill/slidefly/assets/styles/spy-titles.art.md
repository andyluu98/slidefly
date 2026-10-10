# Điệp viên 60s: luật vẽ minh họa SVG cho từng slide

Dùng cùng `spy-titles.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một cảnh trong phần mở đầu của một bộ phim điệp viên chưa từng có: giấy cắt, bốn màu mực, hình bóng đen. Deck mẫu: `gallery/69_demo-spy-titles.html`.

## 1. Tinh thần
- **Bốn màu mực phẳng, đục, trên giấy:** đen mực, kem giấy, đỏ điệp viên, vàng mù tạt. Không gradient, không trong suốt (trừ bóng giấy), không viền mảnh quanh hình.
- **Mép cắt bằng kéo:** mọi hình đa giác đều có cạnh hơi lệch tay, góc vẫn nhọn. **Các mảnh giấy xếp lớp** và đổ một bóng giấy phẳng lệch xuống phải.
- **Trừu tượng hóa tới hình bóng:** người chỉ là một mảng đen (mũ phớt, áo khoác dài, một mảng đỏ là khăn bay). Không mặt, không chi tiết quần áo; diễn xuất nằm ở dáng chạy và nhịp.
- **Chữ là một phần của bối cảnh:** dòng chữ trong hình là một "dòng danh đề" ngắn, in hoa, giữ nguyên là chữ chứ không chồng lên hình bóng.
- Nhịp dựng: các mảnh hiện ra theo thứ tự "cắt giấy dán", không có chuyển động mượt giữa các mảnh; thứ gì cũng dừng đột ngột.
- Mỗi slide là một "địa điểm" có **một màu nền chủ đạo** (đen, kem, đỏ, vàng); hình dùng mã màu cố định nên phải vẽ theo màu nền của đúng kiểu slide nó nằm trên. Vật được săn đuổi là **chiếc chìa khóa đồng** trên nền đen (diễn viên `key` của style).
- Vòng tròn khổng lồ (diễn viên `moon`) là mặt trăng, hình ảnh "bóng đen trước vòng tròn lớn". Không dựng cảnh nòng súng, không súng, không đồ chơi gián điệp.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (hình bóng, dải danh đề) | `#1b1714` |
| Kem (giấy, chữ trên nền tối, vạch chữ giả) | `#efe4c9` |
| Đỏ điệp viên (khăn, một vật nhấn mỗi hình) | `#d23a22` |
| Vàng mù tạt (vật bị săn, ô nhỏ) | `#e2a52a` |
| Bóng giấy | `rgba(0,0,0,.28)`, lệch (7, 9), không làm mờ |

- **Nền mỗi kiểu slide:** cover: đen; agenda, content, timeline, closing: kem; section: đỏ; two-col, quote: đen; stats: vàng. Vật đen trên nền đen thì mất hình: hình bóng chỉ đặt trước mặt trăng kem, vàng hoặc trên nền sáng.
- **Mép cắt:** chia mỗi cạnh thành đoạn khoảng 11px, đẩy từng điểm theo pháp tuyến một đoạn nhỏ (tối đa 1,6px, thỉnh thoảng một vết khía 2,2px); điểm góc giữ nguyên. Cùng một mảnh dùng cùng một mép ở mọi chỗ.
- **Bóng giấy:** vẽ lại đúng đa giác đó trước, tô `rgba(0,0,0,.28)`, dịch `translate(7 9)`.
- Chữ: nhãn tiếng Việt dùng `var(--font-display)` (League Gothic, in hoa, giãn 0,08em, 30px) hoặc `var(--font-body)` (League Spartan 700, 18px, giãn 0,16em); số trên đĩa đỏ dùng chữ kem.
- Khai báo lớp chữ trong `<style>` của deck (`.sp-t .sp-lb .sp-num`, xem deck mẫu). Hình khối dùng thuộc tính `fill` với mã hex ngay trên phần tử để bản PPTX đọc được màu.

## 3. Bộ hình mẫu lặp lại
**Tờ giấy là slide:** hình chữ nhật 16:9 xoay vài độ, mép cắt, hai đến ba vạch kem hoặc đen làm "dòng chữ", thêm một đĩa nhỏ làm hình. Ba cỡ 130, 170, 200px chiều rộng là đủ.
**Hình bóng chạy** (khung 320x510, quay mặt sang phải): áo khoác `M158 100L206 104L218 166L206 258L176 296L128 318L78 338L96 278L122 206L144 140Z`, đầu và mũ phớt (vành `M128 49L150 38L206 34L230 46L206 51L150 55Z`), tay chân là các thanh thuôn (rộng 42 xuống 20), giày là nêm; khăn đỏ `M164 98L186 106L150 102L108 90L64 72L26 82L66 102L110 116L152 120Z`.
Mẫu một tờ giấy (bóng, thân, vạch chữ; cả khối xoay quanh tâm tờ giấy):
```svg
<g transform="rotate(-14 125 238)">
  <path d="M40 190L211 188L210 286L41 285Z" transform="translate(7 9)" fill="rgba(0,0,0,.28)"/>
  <path d="M40 190L211 188L210 286L41 285Z" fill="#d23a22"/>
  <path d="M54 206H196V212H54ZM54 220H174V226H54ZM54 234H196V240H54Z" fill="#efe4c9"/>
</g>
```
(Trong bản thật, mỗi cạnh được chia nhỏ khoảng 11px và lệch nhẹ như mục 2.)
**Mảnh nêm chuyển động:** ba tam giác đen nhỏ dần xếp thành hàng chỉ hướng bay của tờ giấy.
**Dải danh đề:** hình chữ nhật đen dài 540x66 hơi lệch, đĩa đỏ mang số kem ở đầu trái, hai vạch kem ở giữa, một ô vàng vuông nhỏ ở cuối phải.
**Chiếc chìa khóa:** vật vàng đặt trên một đĩa đen cắt tay; luôn là vật sáng nhất trong khung đen.
**Chồng dải:** n dải đen xếp chồng khít, chừa khe 6px; dải bị cắt thì lệch ngang xen kẽ, một dải đổi sang đỏ.
**Đĩa trạm:** đĩa 28px bán kính mép cắt, tô một trong bốn màu, viền đen 5px, chấm đen ở giữa; màu kem thì viền đen để không chìm vào giấy.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm bên trái (x 120 đến 1020). Hình đặt trong x 1040 đến 1920, y 100 đến 800, quanh mặt trăng `moon` (tâm 1470, 470, đường kính 640), hình bóng chạy `fig` (x 1330, y 270) và dải nhà `city` ở đáy (y 822). Hình SVG vẽ ba tờ giấy (đỏ, vàng, đen) bị ném ra sau lưng người chạy, nghiêng lệch nhau, kèm ba mảnh nêm.
- Tờ giấy là ẩn dụ của chủ đề (deck mẫu: ba slide bay theo người chạy). Không để tờ giấy đen ra ngoài mặt trăng.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980), trên mặt trăng vàng của style (tâm 1530, 440, đường kính 480). Chừa dải y 320 đến 380 trong hình (trang y 600 đến 660) cho `hl-text`. Nửa trên: tư thế cũ (tờ nhỏ đen), ba mảnh nêm, tư thế mới (tờ lớn đỏ, vạch kem), nhãn TƯ THẾ A, TƯ THẾ B ở y 306. Nửa dưới: ba dải danh đề đánh số 1, 2, 3 (y 410, 498, 586).
- Một thành phần = một tờ giấy; cùng một vật thì cùng số.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`: trục là một dải đen cắt tay dày 15px chạy suốt chiều ngang. Mỗi bước một "đĩa trạm" ở x = 136 + i x 342,4 (5 bước): bốn đĩa tô đỏ, vàng, kem, đỏ; trạm cuối là nơi chiếc chìa khóa (diễn viên `key`) đáp xuống. Một hình bóng nhỏ (tỷ lệ 0,2) chạy trên trục ở khoảng trống giữa trạm 4 và chữ bước 5. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674) tại những cột có chữ.

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986 dưới mỗi con số: mỗi cột một chồng dải đen mang ý của số (deck mẫu: 3, 5, 7 dải, càng nhiều càng mảnh; chồng bảy dải bị cắt lệch xen kẽ, một dải đỏ, nghĩa là nên tách slide). Tâm cột: x 384, 960, 1536 (ba số). So sánh hai phương án: hai chồng cạnh nhau cùng chiều cao.

## 5. Chuyển động và xuất PPTX
- Mảnh giấy hiện lần lượt bằng `<g class="reveal" style="--i:2">` (không dùng `draw`, vì hình là mảng tô đặc chứ không phải nét). Thứ tự: tờ giấy sau, tờ giấy trước, mảnh nêm, nhãn.
- Không dùng animation lặp, không rung lắc, không đổi màu. Chuyển động giữa hai slide là việc của diễn viên (mặt trăng, người chạy, dải chéo, chìa khóa).
- Cả hình xong trong khoảng 2 giây để người nói không phải chờ.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành một hình vector; phép `transform="rotate(...)"` bên trong được giữ nguyên. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.sp-t`), nên đặt tên lớp riêng có tiền tố.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, tờ giấy đen không nằm trên nền đen, dải y 320 đến 380 trống.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ có bốn màu mực, bóng giấy và (nếu cần) đĩa trạm có viền đen; màu chữ nhãn đủ tương phản với nền slide đó.

## 6. Cấm
- Màu ngoài bốn mực, gradient, glow, blur, độ trong suốt (trừ bóng giấy), viền mảnh quanh hình.
- Nòng súng, súng, cảnh bạo lực, đồ chơi gián điệp; bắt chước chữ, nhân vật hay cảnh của một bộ phim có thật.
- Tên người có thật làm danh đề: chỉ dùng vai hư cấu hoặc nhãn kỹ thuật.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165; để chữ nằm trên hình bóng.
- Ghi số liệu bịa trên hình: dùng nhãn chữ (TƯ THẾ A) hoặc số thứ tự.
- Câu dài trong SVG.

Phỏng theo lemo-opuscar `styles/spy-titles/STYLE.md` (MIT) qua MotionFly.
