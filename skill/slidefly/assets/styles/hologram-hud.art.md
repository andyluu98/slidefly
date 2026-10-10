# HUD hologram: luật vẽ minh họa SVG cho từng slide

Dùng cùng `hologram-hud.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một "ảnh quét" hiện lên trên màn hình HUD. Deck mẫu: `gallery/67_demo-hologram-hud.html`.

## 1. Tinh thần
- Vật thể luôn là **khung dây làm bằng ánh sáng**, không bao giờ là vật được tô đặc: nét mảnh, mặt trong suốt rất nhạt, nằm trên nền gần đen. Mọi thứ trông như **dữ liệu vừa được quét**.
- **Một sắc lạnh duy nhất** (xanh ngọc `--line`), đổi độ mờ để tạo chiều sâu: vật gần sáng, vật xa chìm xuống 25 đến 30%. Trắng ngà `--hot` chỉ dành cho thứ đang "nóng": cạnh vừa quét tới, vật đang được khóa mục tiêu.
- **Số liệu được khóa mới được mang màu cam** `--lock`, và màu này nằm ở chữ của slide (số lớn, mốc thời gian), không bao giờ nằm trong hình SVG.
- Có đủ ba lớp sâu: lưới chấm nền, vật thể trên bệ chiếu, rồi đồ nghề HUD phía trước (khung góc, thước chia, bóng đánh số). Chữ trong hình luôn nằm trên một **tấm nền tối** có tick ở bốn góc, không đè lên nét khung dây.
- Không vẽ người, không vẽ vật thể có thật hay logo. Vật thể là ẩn dụ của chủ đề (deck mẫu: ba tầng slide chồng nhau, một khối có lỗ).

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Cạnh chính (vật gần) | `var(--line)` (#3be8d9), lớp `.hd-w` |
| Cạnh phụ, đường dẫn | `var(--line-soft)` (xanh ngọc 60%), `.hd-d`, `.hd-t` |
| Vật xa, lưới | `var(--hair)` (24%), `.hd-f` |
| Cạnh nóng | `var(--hot)` (#eafffd), `.hd-hot`, `.hd-lk` (khung khóa) |
| Mặt trong suốt | `var(--face)` (xanh ngọc 9%), `.hd-face` |
| Tấm nền chữ | `var(--plate)`, viền `var(--line-soft)`, `.hd-plate` |
| Màu cam số liệu (cấm dùng trong hình) | `var(--lock)` |

- Độ dày trên khung 1920x1080: cạnh chính 2,5px, cạnh nóng 3px, đường dẫn 1,8 đến 2px, vạch chữ giả 6px. `stroke-linecap` và `stroke-linejoin` để `round`.
- Kiểu nét: đường trục "tách rời" `stroke-dasharray: 22 6 4 6` (`.hd-ax`); nét khuất 8 7 (`.hd-hid`, vật ở tư thế cũ); đường chuyển (phantom) `26 6 6 6` (`.hd-ph`).
- Hình khối dựng bằng **phép chiếu đẳng cự** (trục x nghiêng 30 độ): điểm `(cx + (u - v) * 0.866, cy + (u + v) * 0.5 - z)`. Một tấm slide 16:9 trong phép chiếu này: `u` 340, `v` 191, dày 8px.
- Chữ: tiếng Việt dùng `var(--font-display)` (Chakra Petch 500, IN HOA, giãn 0,1em, nhãn 19 đến 24px); số, mã, bóng đánh số dùng `var(--font-mono)` (IBM Plex Mono 600).
- Khai báo lớp nét trong `<style>` của deck (`.hd-w .hd-d .hd-f .hd-hot .hd-face .hd-hid .hd-ax .hd-ph .hd-t .hd-bar .hd-let .hd-seg .hd-lk .hd-ar .hd-plate .hd-bal .hd-lb .hd-mono`, xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Bộ hình mẫu lặp lại
**Tấm nền nhãn** (hộp tối, đánh số, bốn tick góc sáng), đặt sau đường dẫn kết thúc bằng chấm:
```svg
<path class="hd-t" d="M1686 330H1720"/><circle class="hd-ar" cx="1686" cy="330" r="4"/>
<path class="hd-plate" d="M1720 308h120v44h-120z"/><path class="hd-w" d="M1720 308h14M1720 308v12M1840 352h-14M1840 352v-12"/>
<text class="hd-mono" x="1734" y="337">01</text><text class="hd-lb hd-sm" x="1770" y="337">CHỮ</text>
```
**Tầng chồng nhau (nổ theo trục):** mỗi tầng một hình thoi chiếu đẳng cự, tầng đang xét dùng `.hd-hot`, tầng giữa `.hd-d`, tầng đáy `.hd-f`; trục `.hd-ax` xuyên qua các tâm, bóng của vật in xuống bệ bằng hai elip `.hd-f` và `.hd-hid`.
**Khóa mục tiêu:** bốn góc chữ L dài 20 đến 30px, `.hd-lk` (tắt ở slide không cần). Diễn viên `lock` của style đã làm việc này ở cấp slide; trong hình chỉ vẽ lại khi cần khóa một chi tiết nhỏ.
**Hai tư thế của một vật:** tư thế cũ nét khuất `.hd-hid` kèm elip bóng, tư thế mới `.hd-hot` được nhấc lên khỏi bóng, nối bằng `.hd-ph` có mũi tên đặc.
**Đồng hồ cung:** bảy đoạn cung `stroke-width: 16` rộng 180 độ, đoạn sáng `.hd-seg`, đoạn tắt thêm `opacity: .28`, kim bằng một nét `.hd-hot`.
**Thanh vạch:** các vạch đứng `M x y v18` cách nhau 22px, số vạch sáng nói mức độ.
Mẫu đồng hồ cung ba đoạn sáng, bốn đoạn tắt (bảy đoạn rộng 180 độ), tâm (264, 124), bán kính 80:
```svg
<path class="hd-seg hd-arc" d="M184.1 120.6A80 80 0 0 1 190.5 92.3M193.4 86.3A80 80 0 0 1 211.5 63.6M216.8 59.4A80 80 0 0 1 242.9 46.8"/>
<path class="hd-seg hd-arc" style="opacity:.28" d="M249.5 45.3A80 80 0 0 1 278.5 45.3M285.1 46.8A80 80 0 0 1 311.2 59.4M316.5 63.6A80 80 0 0 1 334.6 86.3M337.5 92.3A80 80 0 0 1 343.9 120.6"/>
<path class="hd-hot" style="stroke-width:3" d="M264 124L246 74"/><circle class="hd-bal" cx="264" cy="124" r="8"/>
```
**Nhãn hình** góc trên trái: `QUÉT n · TÊN` kèm gạch chân `.hd-t`.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm trên tấm nền bên trái (x 96 đến 1056). Hình đặt trong x 1060 đến 1840, y 100 đến 860, tâm x 1450 trùng với bệ chiếu `pad`, nón sáng `beam` và vòng đo `ring` của style; khung khóa `lock` ôm tầng trên cùng, dải quét `scan` cắt ngang ở y 300.
- Lớp vẽ: nhãn quét, trục tách rời, bóng trên bệ, các tầng từ đáy lên đỉnh (tầng đỉnh có `draw`), đường dẫn và tấm nền nhãn bên phải.
- Ba tầng cách nhau 130px (tâm y 190, 330, 470 trong hình), tầng ở trên mang ý chính của chủ đề.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980), trong khung khóa của style. Chừa dải y 320 đến 380 trong hình (trang y 600 đến 660) cho `hl-text`. Nửa trên: các thành phần là khối chiếu đẳng cự nối bằng đường phantom có mũi tên, mỗi thành phần một bóng số, nhãn tư thế dưới bóng đổ. Nửa dưới: bảng thông số (tấm nền, ba hàng: số, tên bằng vạch, mức bằng thanh vạch).
- Cùng một vật thì cùng số (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; diễn viên `scan` đã là đường trục sáng và `ruler` là thước chia bên dưới. Mỗi bước một "trạm" (ô vuông tối có bốn tick góc và chấm tâm) ở x = 136 + i x 342,4 (5 bước), đường dóng mảnh lên xuống 44px. Giữa hai trạm là một đoạn `.hd-hot draw` chạy sáng kèm đầu mũi tên đặc (mỗi đoạn trễ thêm 0,2 giây). Trạm cuối thêm bốn góc khóa `.hd-lk`. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986 dưới mỗi con số: mỗi cột một đồng hồ cung bảy đoạn, số đoạn sáng tăng dần (3, 5, 7) theo ý của con số; đồng hồ đầy được đổi sang `.hd-hotseg` và đóng khung khóa để nói "quá tải, hãy tách". Tâm cột: x 384, 960, 1536 (ba số). So sánh hai phương án: hai đồng hồ hoặc hai khối cạnh nhau cùng tỷ lệ, cùng thang vạch.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"` (giây trễ), cần `morph-motion.css`. Thứ tự quét: cạnh nóng trước, rồi đường dẫn, tấm nền nhãn và số. Không gắn `draw` vào nét đứt (`.hd-ax`, `.hd-hid`, `.hd-ph`) vì `draw` ghi đè `stroke-dasharray`.
- Nhãn, bóng số, bảng thông số: bọc `<g class="reveal">` để hiện sau nét.
- Không dùng animation lặp, không nhấp nháy, không rung. Hiệu ứng "chữ số lăn" và "xóa quét" của video không mang sang slide; chỉ dùng diễn viên `scan`.
- Cả hình xong trong khoảng 2 giây để người nói không phải chờ.
- Nhịp gợi ý: cạnh nóng `--d:0`, đường dẫn `--d:.3`, mỗi đoạn chạy sáng của quy trình trễ thêm 0,2 giây; nhãn và bảng hiện sau bằng `reveal`.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành một hình vector, hiện bằng hiệu ứng quét nếu bên trong có `draw`. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.hd-w`), nên đặt tên lớp riêng có tiền tố. Màu mờ viết bằng `var()` hoặc `rgba`, không dùng `filter`, `mix-blend-mode`.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn kỹ thuật ngắn, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không lệch khỏi trục và khung khóa của diễn viên. Chữ trong hình không nằm trên nét khung dây.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ có `var(--line)`, `var(--line-soft)`, `var(--hair)`, `var(--hot)`, `var(--face)`, `var(--plate)`, `var(--fg)` hoặc mã xanh ngọc tương đương. Không có màu cam.

## 6. Cấm
- Màu ngoài bảng (nhất là cam trong hình SVG), gradient màu, bóng đổ màu, hiệu ứng glow neon, mặt đặc che hết khung dây.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Ghi số đo hoặc số liệu bịa trên nhãn và đồng hồ: dùng nhãn chữ (TƯ THẾ A, CHỮ, HÌNH, NỀN) hoặc số thứ tự.
- Logo thật, sản phẩm có thật (xe, điện thoại, máy bay có thương hiệu), giao diện của phim cụ thể.
- Câu dài trong SVG; người vẽ thay cho vật được quét.

Phỏng theo lemo-opuscar `styles/hologram-hud/STYLE.md` (MIT) qua MotionFly.
