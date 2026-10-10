# Pictogram: luật vẽ minh họa SVG cho từng slide

Dùng cùng `pictogram.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một tấm thẻ trong bộ nhận diện thể thao: khối màu phẳng, thanh bo tròn, một nhân vật người que. Deck mẫu: `gallery/68_demo-pictogram.html`.

## 1. Tinh thần
- **Một mực đen, vài khối màu phẳng.** Mọi hình là đĩa, bán nguyệt, thanh bo tròn đầu và hình chữ nhật bo góc. Không viền mảnh, không bóng, không gradient (ánh quét sáng là việc của diễn viên `sun`).
- **Người que kiểu Olympic:** đầu là một đĩa, thân và tay chân là các thanh bo tròn đầu; không mặt, không biểu cảm, không quần áo. Tay chân phía xa cùng màu với thân nhưng mờ còn 45%. Một hình người chỉ làm một việc (chạy, đứng, giơ tay).
- **Lưới vuông chặt:** mọi khối đặt theo ô 180px của style; hình minh họa mượn đúng ngôn ngữ đó (đĩa theo hàng, thẻ xếp chồng, thanh vạch đều).
- Mỗi slide là một "chương" mang một màu nền (vàng, kem, tím, xanh lá, đỏ, mực); hình SVG dùng mã màu cố định bên dưới nên phải vẽ theo màu nền của đúng kiểu slide nó nằm trên.
- Chữ trong hình là nhãn mono ngắn, in hoa, giống chữ meta ở góc thẻ phát sóng. Chữ lớn thuộc về slide, không thuộc hình.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (nét, người que, thanh) | `#1b1712` |
| Kem (thẻ, đĩa trên nền đỏ, chữ số trên đĩa màu) | `#f7f0de` |
| Vàng sáng (đĩa cắt, vùng sáng) | `#fbe08a` |
| Bộ màu chương | đỏ `#bf3620`, tím `#4e3392`, xanh lá `#17633d`, vàng `#f5b90a` |
| Nền theo kiểu slide | cover, closing: vàng; agenda, content, timeline: kem; section: tím; two-col: xanh lá; stats: đỏ; quote: mực |

- Độ dày trên khung 1920x1080: thanh bo tròn 22px (mảnh 18px), đường mặt đất 6px, trục quy trình 10px, viền thẻ 6px, viền viên thuốc 4px, vạch chia 5px. `stroke-linecap` để `round`.
- Hình khối chỉ có **tô phẳng**: mỗi khối một màu, không viền ngoài trừ thẻ giấy (viền mực 6px). Cấm bóng đổ, cấm gradient màu.
- Chữ: nhãn dùng `var(--font-mono)` (IBM Plex Mono 600), 18 đến 22px, giãn 0,1em, in hoa; số trên đĩa màu dùng chữ kem 24px.
- Khai báo lớp nét trong `<style>` của deck (`.pg-bar .pg-ground .pg-axis .pg-stub .pg-arrow .pg-ring .pg-card .pg-ghost .pg-ghostd .pg-pill .pg-tick .pg-cream .pg-gold .pg-base .pg-mono`, xem deck mẫu) để bản PPTX đọc được màu và nét. Dùng mã màu hex trong lớp, không dùng `var(--fg)` vì màu chữ đổi theo từng chương.

## 3. Bộ hình mẫu lặp lại
**Người que** (khung 400x500, đầu r 44, thân 64px; đặt vào slide bằng `transform="translate(x y) scale(k)"`). Tư thế chạy:
```svg
<path d="M228 152L318 214L384 168" stroke="#1b1712" stroke-opacity=".45" stroke-width="32" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M212 296L300 376L252 478" stroke="#1b1712" stroke-opacity=".45" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M236 130L206 288" stroke="#1b1712" stroke-width="64" fill="none" stroke-linecap="round"/>
<path d="M238 152L158 224L102 166" stroke="#1b1712" stroke-width="34" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M204 296L128 388L50 462" stroke="#1b1712" stroke-width="42" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="246" cy="56" r="44" fill="#1b1712"/>
```
Thứ tự vẽ: tay chân xa, thân, tay chân gần, đầu. Tư thế đứng: tay chân buông thẳng. Tư thế giơ tay: hai tay chữ V lên trên, hai chân dạng. **Tư thế cũ** của cùng một người thì bọc `<g opacity=".4">`.
**Đường mặt đất:** `M x y H x2`, `.pg-ground draw`, người đứng sát mép dưới chân.
**Thanh tốc độ:** ba thanh `.pg-bar` ngắn, độ mờ 35 đến 50%, đặt sau lưng người chạy.
**Thẻ chồng kiểu "bóng ảnh cũ":** hai thẻ nét đứt `.pg-ghost` (kèm vòng tròn nhỏ `.pg-ghostd`) phía sau, một thẻ đặc `.pg-card` phía trước mang đĩa lớn; cùng một đĩa lớn dần khi sang slide mới.
Mẫu ba thẻ chồng (tọa độ trong hình bìa, thẻ 220x124, mỗi thẻ lệch 50 sang phải, 40 đến 50 xuống dưới):
```svg
<rect class="pg-ghost" x="470" y="326" width="220" height="124" rx="16"/><circle class="pg-ghostd" cx="520" cy="364" r="16"/>
<rect class="pg-ghost" x="520" y="376" width="220" height="124" rx="16"/><circle class="pg-ghostd" cx="557" cy="410" r="22"/>
<rect class="pg-card" x="570" y="416" width="220" height="124" rx="16"/><circle fill="#bf3620" cx="680" cy="478" r="44"/>
```
Mẫu một viên thuốc (cao 72, tâm hàng y 430): `<rect class="pg-pill" x="2" y="394" width="536" height="72" rx="36"/>`, đĩa số `<circle fill="#bf3620" cx="38" cy="430" r="26"/>`, thanh tên `<path class="pg-bar pg-thin" d="M100 430H230M250 430H300"/>`, vạch chia `<path class="pg-tick" d="M360 420v20M384 420v20M408 410v40"/>`.
**Viên thuốc đánh số:** hình chữ nhật bo tròn hết cỡ `rx` bằng nửa cao, đĩa màu chương ở đầu trái mang số kem, thanh bo tròn là tên, bảy vạch chia ở bên phải trong đó một vạch cao hơn.
**Hàng đĩa:** n đĩa đều nhau trong chiều ngang 400px, bán kính 0,36 bước; bán nguyệt vàng sáng (bán kính 0,46 bước) khi muốn nói "bị cắt".

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm bên trái (x 120 đến 1000). Hình đặt trong x 1040 đến 1920, y 100 đến 960, quanh đĩa `sun` (tâm 1440, 540, đường kính 720) và người chạy của style (diễn viên `run`, chân chạm y 632). Lớp vẽ: thanh tốc độ, đường mặt đất (trang y 640), rồi ba thẻ chồng ở phải, thẻ trước đè lên đường mặt đất.
- Vật là ẩn dụ của chủ đề (deck mẫu: ba thẻ slide, đĩa đỏ lớn dần cho "slide biết chuyển cảnh"). Không ghi số đo.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980), trên đĩa `sun` (tâm 1530, 430, đường kính 400). Chừa dải y 320 đến 380 trong hình (trang y 600 đến 660) cho `hl-text`. Nửa trên: tư thế cũ mờ 40%, mũi tên thanh bo tròn, tư thế mới đặc, chung một đường mặt đất; nhãn TƯ THẾ A, TƯ THẾ B ngay dưới (y 304). Nửa dưới: ba viên thuốc đánh số 1, 2, 3, mỗi viên một màu chương.
- Một thành phần = một tư thế hoặc một khối; cùng một vật thì cùng số (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; trục là một thanh mực dày 10px do chính hình vẽ (`.pg-axis draw`). Mỗi bước một "trạm" (đĩa màu chương r 26, viền mực 6px, lõi kem r 8) ở x = 136 + i x 342,4 (5 bước), đường dóng 44px lên xuống; trạm cuối thêm vòng ngoài r 40. Một người que nhỏ (tỷ lệ 0,22) đứng trên trục ở khoảng trống giữa trạm 4 và chữ bước 5, kèm hai thanh tốc độ. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674) tại những cột có chữ.

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986 dưới mỗi con số: mỗi cột một hàng khối nói ý của số (deck mẫu: 3, 5, 7 đĩa càng nhiều càng nhỏ; hàng bảy là bán nguyệt vàng sáng = bị cắt, nên tách slide), kèm vạch nền kem. Tâm cột: x 384, 960, 1536 (ba số). So sánh hai phương án: hai hàng cùng chiều rộng, khác số khối hoặc khác màu chương.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"` (giây trễ), cần `morph-motion.css`. Chỉ gắn `draw` vào mặt đất, trục, mũi tên; các khối đặc hiện bằng `reveal`, thẻ chồng lần lượt với `--i`.
- Không dùng animation lặp, không đổi màu, không rung lắc. Chuyển động giữa hai slide là việc của diễn viên (đĩa, bán nguyệt, người que trượt trên lưới).
- Cả hình xong trong khoảng 2 giây để người nói không phải chờ.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành một hình vector, hiện bằng hiệu ứng quét nếu bên trong có `draw`. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.pg-bar`), nên đặt tên lớp riêng có tiền tố. Người que vẽ bằng thuộc tính `stroke`, `stroke-opacity` ngay trên phần tử.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn mono ngắn, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, người que đứng đúng trên mặt đất, hình không lệch khỏi đĩa `sun` và dải y 320 đến 380.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ có mực, kem, vàng sáng và bốn màu chương; màu chữ nhãn đủ tương phản với nền của slide đó.

## 6. Cấm
- Màu ngoài bảng, gradient, bóng đổ, viền mảnh quanh khối, hiệu ứng blur hay glow.
- Người có mặt, biểu cảm, quần áo, tóc; nhiều hình người làm nhiều việc trong một hình.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Ghi số liệu bịa trên hình: dùng nhãn chữ (TƯ THẾ A) hoặc số thứ tự.
- Bắt chước pictogram, biểu trưng, tên hay khẩu hiệu của một sự kiện thể thao có thật; lấy bộ màu và họa tiết từ chính chủ đề của deck.
- Câu dài trong SVG.

Phỏng theo lemo-opuscar `styles/pictogram-motion/STYLE.md` (MIT) qua MotionFly.
