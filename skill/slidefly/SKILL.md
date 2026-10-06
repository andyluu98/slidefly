---
name: slidefly
description: Tạo slide HTML có hiệu ứng chuyển cảnh kiểu PowerPoint Morph (hình trang trí trượt, phóng to, đổi màu liền mạch giữa các slide), 57 style, bố cục tự lấp đầy theo lượng chữ và tự đo độ trống của từng slide, 8 dạng sơ đồ tự vẽ từ số liệu, hiệu ứng theo động từ và bấm từng bước. Dùng khi người dùng nói "slide morph", "slide animation đẹp", "slide HTML có hiệu ứng chuyển cảnh", "làm deck chuyển động", "/slidefly", "SlideFly", hoặc muốn chuyển một mẫu PowerPoint Morph sang web. Không dùng khi cần file .pptx chỉnh sửa được (dùng office-docs hoặc pptx) hay chỉ cần slide HTML hiệu ứng xuất hiện đơn giản (frontend-slides).
---

# SlideFly: slide biết bay

Slide HTML một file, trình chiếu bằng Chrome/Edge. Hình trang trí ("diễn viên") sống trên một sân khấu chung; mỗi kiểu slide là một "tư thế". Chuyển slide thì diễn viên trượt sang tư thế mới, đúng tinh thần Morph: cùng tên là cùng một vật.

Skill dir: `~/.claude/skills/slidefly/` (gọi tắt `$SK`). Python 3.10+ có Playwright + Pillow: `pip install -r requirements.txt` rồi `playwright install chromium`.

```
assets/morph-base.css      khung 1920x1080, diễn viên, reveal, giảm chuyển động
assets/morph-layouts.css   9 kiểu slide, tự co giãn theo data-density
assets/morph-layouts-plus.css  12 kiểu mới: big-number, bento, split-photo, qa, before-after, process, compare-table, portrait-quote, chapter, countdown, statement, cta
assets/morph-engine.js     co giãn khung, tạo diễn viên từ --actors, FLIP, mật độ
assets/morph-nav.js        phím, 2 nút mũi tên ở hai rìa, vuốt, #số-slide (bấm vào thân slide không chuyển)
assets/morph-audit.js      deck.audit(): đo khoảng trống, tràn chữ, slide lặp kiểu, biểu đồ thiếu nguồn
assets/morph-motion.css    hiệu ứng theo động từ (vẽ nét, đếm, đóng dấu, rơi, gộp...) + màu --viz-*
assets/morph-viz.css       giao diện 8 dạng sơ đồ
assets/morph-viz.js        vẽ sơ đồ từ data-*: span, donut, plan, gather (nạp sau morph-viz-diagrams.js)
assets/morph-viz-diagrams.js  matrix, network, funnel, compare
assets/morph-steps.js      bấm từng bước: data-step, data-at
assets/morph-brand.css     logo xuyên suốt: to ở bìa, nhỏ ở góc, ẩn ở trích dẫn, tự bay giữa các slide
assets/morph-mock.css/.js  khung giao diện giả: chat, terminal, trình duyệt, điện thoại; chữ gõ dần, dòng hiện lần lượt
assets/morph-photo.css     slide ảnh nền tràn màn hình (data-layout="photo"), lớp phủ giữ chữ dễ đọc
assets/morph-icons.css/.js icon Tabler: <i class="ico" data-icon="...">, tự tải khi soạn, nhúng khi gộp
assets/icons/              danh mục Tabler (tabler-index.json) + từ khóa tiếng Việt (vi-keywords.json)
assets/styles/*.css        57 style; assets/styles/index.json = tên, nền, nhãn tâm trạng, hợp với, font
templates/deck-mau.html    deck mẫu 10 slide đủ 9 kiểu: KHUNG ĐỂ COPY
templates/deck-so-do.html  deck mẫu 16 slide: mỗi slide một dạng hình, có bấm từng bước
templates/deck-bo-cuc.html  deck mẫu 13 slide: đủ 12 bố cục mới
templates/deck-giao-dien.html  deck mẫu 10 slide: logo xuyên suốt, 4 khung giao diện, lưới icon, ảnh nền
scripts/inline-assets.py   gộp CSS/JS thành 1 file HTML mang đi được
scripts/check-deck.py      chụp mọi slide + đo + bắt lỗi console, ra sheet.jpg
scripts/icons.py           search <từ> / suggest <deck.html>: tìm và gợi ý icon Tabler
scripts/build-gallery.py   dựng demo + trang 00-gallery.html xem/lọc mọi style
scripts/pick-styles.py     gợi ý 3 style (hợp, khác nền, bất ngờ) + 1 cách kể, xáo mỗi lần chạy, không lặp style vừa dùng
```

Đọc thêm khi cần: `references/layouts.md` (markup từng kiểu slide), `references/co-che-morph.md` (cơ chế, viết style mới, port PowerPoint), `references/vu-dao-morph.md` (công thức chuyển cảnh), `references/style-presets.md` (chọn style), `references/hieu-ung-va-so-do.md` (chọn hình theo ý, khai báo sơ đồ, hiệu ứng, bấm từng bước), `references/icon-tabler.md` (icon: tìm, khai báo, luật chống rối), `references/logo-va-giao-dien.md` (logo xuyên suốt, khung chat/terminal/trình duyệt/điện thoại, slide ảnh nền, lưới icon).

## Quy trình

### Bước 1. Nhận nội dung
- File `.docx/.pdf/.pptx` thì convert bằng markitdown trước khi đọc.
- Hỏi gộp một lượt bằng AskUserQuestion (mỗi câu có 2-4 phương án): mục đích và người xem; số slide; mức chữ (ít chữ để thuyết trình / nhiều chữ để đọc); **chất mong muốn** (ví dụ trang trọng, trẻ trung, bản sắc Việt, công nghệ; người dùng gõ chữ khác cũng được). Bỏ câu nào người dùng đã trả lời.
- **Chống rập khuôn:** nhiều người gõ cùng một prompt vẫn phải ra deck khác nhau. Không mặc định chọn cùng một style hay cùng một thứ tự kiểu slide; luôn chạy `pick-styles.py` ở Bước 2 trừ khi người dùng đã nêu tên style.
- Lập dàn ý theo **cách kể** mà `pick-styles.py` bốc ra (mở bằng câu hỏi, bằng con số, bằng tình huống, hoặc kết luận trước); nội dung không hợp cách đó thì chọn cách gần nhất. Mỗi slide một ý, gán sẵn kiểu slide (bảng chọn ở `references/layouts.md`, gồm 9 kiểu gốc và 12 kiểu mới; ý có dáng riêng như con số, quy trình, so sánh, câu hỏi thì dùng kiểu mới tương ứng) và **dạng hình theo ý**: quy trình, so sánh, tỷ lệ, phân loại, lọc dần... mỗi loại một hình (bảng ở `references/hieu-ung-va-so-do.md` mục 2). Không để quá 2 slide liền cùng một kiểu.
- **Số liệu phải có nguồn.** Không bịa số cho `.hl-big` hay `.stat-num`. Không có số thật thì dùng icon hoặc câu chốt.

### Bước 2. Chọn style kiểu "xem rồi chọn"
- Người dùng đã nêu tên style thì dùng đúng style đó. Nếu chưa, chạy:
  `python "$SK/scripts/pick-styles.py" "<mục đích, người xem, chất mong muốn>"`
  Script trả 3 style (hợp, khác nền, bất ngờ) và 1 cách kể, xáo ngẫu nhiên mỗi lần, bỏ qua style máy này vừa dùng. Dùng đúng 3 style đó, không tự thay bằng style "an toàn" quen tay (nhóm gợi ý chỉ để tham khảo: `references/style-presets.md`).
- Dựng 1 file nguồn gồm 3 slide của chính nội dung người dùng (cover, agenda, 1 content), rồi sinh 3 bản chỉ khác dòng link style.
- Người dùng muốn xem hết: chạy `build-gallery.py <thu-muc>` rồi mở `00-gallery.html` (ảnh bìa + slide nội dung của mọi style, lọc theo nền và từ khóa).
- Gộp từng bản bằng `inline-assets.py`, lưu ở scratchpad, gửi cho người dùng (SendUserFile hoặc mở ở trình duyệt). Không ghi tên nội bộ lên slide.
- Người dùng chọn A/B/C hoặc "trộn" (ví dụ màu của A, diễn viên của B: khi đó viết style mới theo `references/co-che-morph.md`).

### Bước 3. Dựng deck
- Copy cấu trúc `templates/deck-mau.html`: `<link>` tới `morph-base.css`, `morph-layouts.css` (thêm `morph-layouts-plus.css` khi dùng 12 kiểu mới), 1 file style; cuối body lần lượt `morph-engine.js`, `morph-nav.js`, `morph-audit.js` (thiếu audit thì `check-deck.py` báo lỗi). Href dùng đường dẫn tuyệt đối tới `$SK/assets/...` khi file nguồn nằm ngoài skill.
- Không viết khối `.actors`: engine tự tạo diễn viên từ `--actors` của style.
- Slide có sơ đồ: dùng `data-layout="diagram"` (hình trang trí dạt ra viền theo tư thế của slide mục lục; cần sân khấu trống hẳn thì thêm `data-stage="clear"`), nạp thêm `morph-motion.css`, `morph-viz.css`, `morph-viz-diagrams.js`, `morph-viz.js` (trước engine) và `morph-steps.js` (sau engine). Hiệu ứng chọn theo động từ của câu (`fx-growx` cho "tăng", `draw` cho "nối", `slam` cho "chốt", `shake` cho "lệch"...). Ý cần giảng lần lượt thì gắn `data-step` (phím lùi gỡ từng bước). Chi tiết: `references/hieu-ung-va-so-do.md`.
- Chống nhàm trong deck dài: khung giao diện đổi bên trái/phải giữa các slide; slide chương xen kẽ nền bằng `data-stage="closing"` (kèm `data-brand="corner"` để logo không phóng to); không để quá 3 slide liền dùng cùng một thành phần. Muốn đổi nhịp, gắn `data-title="center"` lên slide nội dung (content, two-col, stats, timeline, agenda, diagram): tiêu đề ra giữa thay vì góc trái; xen kẽ vài slide trong deck dài.
- Icon: chỉ dùng Tabler qua `<i class="ico" data-icon="...">` (nạp `morph-icons.css` + `morph-icons.js`). Chạy `icons.py suggest nguon.html` để xem gợi ý, rồi tự chọn theo ý chính. Mỗi slide một cách dùng: 1 icon chính, hoặc 1 dải tối đa 6 icon, hoặc icon làm nút sơ đồ; không gắn icon vào từng gạch đầu dòng. Chi tiết: `references/icon-tabler.md`.
- Deck có đơn vị, thương hiệu hay tên khóa học: thêm logo xuyên suốt (`morph-brand.css`, một thẻ `.brand` đặt trong `.deck-stage`). Slide cần cho thấy phần mềm đang chạy (prompt AI, lệnh cài, trang web, app): dùng khung giao diện giả (`morph-mock.css` + `morph-mock.js` trước engine) thay cho ảnh chụp màn hình, tối đa một khung mỗi slide. Cần điểm nghỉ giữa các phần: slide ảnh nền `data-layout="photo"` (ảnh có giấy phép, bắt buộc `.photo-credit`). 3 đến 6 ý ngắn: lưới icon `.ico-grid` trên slide agenda. Chi tiết: `references/logo-va-giao-dien.md`.
- Mỗi `<section class="slide" data-layout="...">`; phần tử nội dung gắn `reveal`, `reveal-left`, `reveal-right`, `reveal-scale` hoặc `reveal-blur`.
- Quy tắc chống trống (bắt buộc):
  - `content`: luôn có `<aside class="highlight">` (icon, số có nguồn, hoặc câu chốt ngắn) ở vùng bên phải.
  - `two-col`: mỗi cột 3 ý trở xuống thì thêm `<p class="takeaway">` câu kết luận.
  - Tối đa 6 ý mỗi slide; hơn thì tách slide. Engine tự chọn cỡ chữ lg/md/sm theo số ý.
  - Dùng `data-morph-id` cùng giá trị cho tiêu đề mục ở agenda và tiêu đề section ngay sau nó để chữ bay sang.
- Văn bản: tiếng Việt có dấu, câu ngắn, **không dùng ký tự gạch ngang dài**.
- Chữ chỉ nằm trong vùng trống của tư thế, hoặc nằm hẳn trên một hình đủ tương phản. Câu dài thì cho xuống dòng hoặc thu hẹp khối chữ, không để chữ kéo qua tấm nền khác màu (nửa dòng trên nền tối, nửa dòng trên nền sáng là mất chữ). Màu nhấn sáng (vàng, xanh lá) đặt trên nền sáng thì đổi sang tông đậm.

### Bước 4. Gộp thành 1 file
```bash
python "$SK/scripts/inline-assets.py" nguon.html "<thu-muc-dich>/NN_ten-deck.html"
```
Tên file theo quy tắc đánh số `NN_` của thư mục đích; báo cáo/bài trình bày để ở thư mục dự án quy định (ví dụ `04-bao-cao/`). Ghi đè file cũ thì sao lưu vào `_backup/` trước.

### Bước 5. Tự kiểm tra (không bỏ qua)
```bash
python "$SK/scripts/check-deck.py" "<file.html>" "<scratchpad>/shots/<ten>"
```
- Phải ra `RESULT: OK`. Rồi **Read `sheet.jpg`** để nhìn cả deck: chữ đè hình, tương phản, lệch.
- Sửa theo lỗi đo được:

| Báo lỗi | Cách sửa |
|---|---|
| `trống dọc` | thêm highlight/takeaway, gộp 2 slide thưa thành 1, hoặc đặt `data-density="lg"` |
| `trống ngang` | slide content thiếu `.highlight`, thêm vào |
| `chữ khó đọc trên hình X` | chữ nằm trên hình trang trí X có độ tương phản dưới 3:1: thu hẹp hoặc dời khối chữ ra khỏi hình, hoặc đổi màu chữ cho slide/tư thế đó |
| `tràn khung` / `chữ tràn hộp` | rút gọn câu, tách slide, hoặc `data-density="sm"` |
| `nhàm: giống hệt 2 slide trước` | đổi dạng hình hoặc hiệu ứng của slide đó (bảng chọn hình theo ý) |
| `NHÀM: slide X-Y: 3 slide liền cùng ...` (nhắc, không chặn) | đổi thành phần của slide giữa: khung giao diện sang bên kia, thay sơ đồ bằng bento/so sánh, hoặc chen một slide statement/qa |
| `quá nhiều icon` / `icon không tồn tại` | giữ icon cho ý chính; tìm đúng tên bằng `icons.py search` |
| `biểu đồ ... thiếu data-source` | ghi nguồn số liệu vào `data-source`; không có nguồn thì bỏ biểu đồ có số |
| lỗi console | đọc thông báo, sửa markup/đường dẫn |

- Slide trưng bày (cover, section, quote, closing) cố ý thoáng nên chỉ bị kiểm tra tràn.
- Trình duyệt trong app có thể chụp lẫn khung hình đang chuyển; dùng `check-deck.py` để xem trạng thái cuối.

### Bước 6. Bàn giao
- Nêu đường dẫn tuyệt đối, số slide, các style đã dùng.
- Cách trình chiếu: mũi tên phải, Space, PageDown hoặc nút `›` ở rìa phải để sang; mũi tên trái hoặc nút `‹` ở rìa trái để lùi; `F` toàn màn hình, `Home`/`End`. Bấm vào thân slide không chuyển, nên bôi đen và chép chữ thoải mái; lăn chuột cũng không chuyển.
- File cần mạng để tải font Google; không mạng thì chữ dùng font dự phòng.
- Nếu Windows tắt "Animation effects", trình duyệt bật chế độ giảm chuyển động: Morph vẫn chạy nhưng ngắn (0,7 giây). Bật lại ở Settings, Accessibility, Visual effects để có hiệu ứng đầy đủ.

