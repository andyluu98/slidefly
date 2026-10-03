---
name: morph-slides
description: Tạo slide HTML có hiệu ứng chuyển cảnh kiểu PowerPoint Morph (hình trang trí trượt, phóng to, đổi màu liền mạch giữa các slide), 47 style, bố cục tự lấp đầy theo lượng chữ và tự đo độ trống của từng slide. Dùng khi người dùng nói "slide morph", "slide animation đẹp", "slide HTML có hiệu ứng chuyển cảnh", "làm deck chuyển động", "/morph-slides", hoặc muốn chuyển một mẫu PowerPoint Morph sang web. Không dùng khi cần file .pptx chỉnh sửa được (dùng office-docs hoặc pptx) hay chỉ cần slide HTML hiệu ứng xuất hiện đơn giản (frontend-slides).
---

# morph-slides

Slide HTML một file, trình chiếu bằng Chrome/Edge. Hình trang trí ("diễn viên") sống trên một sân khấu chung; mỗi kiểu slide là một "tư thế". Chuyển slide thì diễn viên trượt sang tư thế mới, đúng tinh thần Morph: cùng tên là cùng một vật.

Skill dir: `~/.claude/skills/morph-slides/` (gọi tắt `$SK`). Python 3.10+ có Playwright + Pillow: `pip install -r requirements.txt` rồi `playwright install chromium`.

```
assets/morph-base.css      khung 1920x1080, diễn viên, reveal, giảm chuyển động
assets/morph-layouts.css   9 kiểu slide, tự co giãn theo data-density
assets/morph-engine.js     co giãn khung, tạo diễn viên từ --actors, FLIP, mật độ
assets/morph-nav.js        phím, click, vuốt, cuộn chuột, #số-slide
assets/morph-audit.js      deck.audit(): đo khoảng trống, tràn chữ
assets/styles/*.css        47 style; assets/styles/index.json = tên, nền, nhãn tâm trạng, hợp với, font
templates/deck-mau.html    deck mẫu 10 slide đủ 9 kiểu: KHUNG ĐỂ COPY
scripts/inline-assets.py   gộp CSS/JS thành 1 file HTML mang đi được
scripts/check-deck.py      chụp mọi slide + đo + bắt lỗi console, ra sheet.jpg
scripts/build-gallery.py   dựng demo + trang 00-gallery.html xem/lọc mọi style
```

Đọc thêm khi cần: `references/layouts.md` (markup từng kiểu slide), `references/co-che-morph.md` (cơ chế, viết style mới, port PowerPoint), `references/vu-dao-morph.md` (công thức chuyển cảnh), `references/style-presets.md` (chọn style).

## Quy trình

### Bước 1. Nhận nội dung
- File `.docx/.pdf/.pptx` thì convert bằng markitdown trước khi đọc.
- Hỏi gộp một lượt bằng AskUserQuestion (mỗi câu có 2-4 phương án): mục đích và người xem; số slide; mức chữ (ít chữ để thuyết trình / nhiều chữ để đọc). Bỏ câu nào người dùng đã trả lời.
- Lập dàn ý: mỗi slide một ý, gán sẵn kiểu slide (bảng chọn ở `references/layouts.md`).
- **Số liệu phải có nguồn.** Không bịa số cho `.hl-big` hay `.stat-num`. Không có số thật thì dùng icon hoặc câu chốt.

### Bước 2. Chọn style kiểu "xem rồi chọn"
- Lọc `assets/styles/index.json` theo nền (dark/light/mixed), nhãn `mood` và `best_for` khớp với mục đích. Chọn 3 style: 1 an toàn + 2 khác biệt (gợi ý ở `references/style-presets.md`).
- Dựng 1 file nguồn gồm 3 slide của chính nội dung người dùng (cover, agenda, 1 content), rồi sinh 3 bản chỉ khác dòng link style.
- Người dùng muốn xem hết: chạy `build-gallery.py <thu-muc>` rồi mở `00-gallery.html` (ảnh bìa + slide nội dung của mọi style, lọc theo nền và từ khóa).
- Gộp từng bản bằng `inline-assets.py`, lưu ở scratchpad, gửi cho người dùng (SendUserFile hoặc mở ở trình duyệt). Không ghi tên nội bộ lên slide.
- Người dùng chọn A/B/C hoặc "trộn" (ví dụ màu của A, diễn viên của B: khi đó viết style mới theo `references/co-che-morph.md`).

### Bước 3. Dựng deck
- Copy cấu trúc `templates/deck-mau.html`: `<link>` tới `morph-base.css`, `morph-layouts.css`, 1 file style; cuối body lần lượt `morph-engine.js`, `morph-nav.js`, `morph-audit.js` (thiếu audit thì `check-deck.py` báo lỗi). Href dùng đường dẫn tuyệt đối tới `$SK/assets/...` khi file nguồn nằm ngoài skill.
- Không viết khối `.actors`: engine tự tạo diễn viên từ `--actors` của style.
- Mỗi `<section class="slide" data-layout="...">`; phần tử nội dung gắn `reveal`, `reveal-left`, `reveal-right`, `reveal-scale` hoặc `reveal-blur`.
- Quy tắc chống trống (bắt buộc):
  - `content`: luôn có `<aside class="highlight">` (icon, số có nguồn, hoặc câu chốt ngắn) ở vùng bên phải.
  - `two-col`: mỗi cột 3 ý trở xuống thì thêm `<p class="takeaway">` câu kết luận.
  - Tối đa 6 ý mỗi slide; hơn thì tách slide. Engine tự chọn cỡ chữ lg/md/sm theo số ý.
  - Dùng `data-morph-id` cùng giá trị cho tiêu đề mục ở agenda và tiêu đề section ngay sau nó để chữ bay sang.
- Văn bản: tiếng Việt có dấu, câu ngắn, **không dùng ký tự gạch ngang dài**.

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
| `tràn khung` / `chữ tràn hộp` | rút gọn câu, tách slide, hoặc `data-density="sm"` |
| lỗi console | đọc thông báo, sửa markup/đường dẫn |

- Slide trưng bày (cover, section, quote, closing) cố ý thoáng nên chỉ bị kiểm tra tràn.
- Trình duyệt trong app có thể chụp lẫn khung hình đang chuyển; dùng `check-deck.py` để xem trạng thái cuối.

### Bước 6. Bàn giao
- Nêu đường dẫn tuyệt đối, số slide, các style đã dùng.
- Cách trình chiếu: mũi tên/Space/click để sang, mũi tên trái để lùi, `F` toàn màn hình, `Home`/`End`.
- File cần mạng để tải font Google; không mạng thì chữ dùng font dự phòng.
- Nếu Windows tắt "Animation effects", trình duyệt bật chế độ giảm chuyển động: Morph vẫn chạy nhưng ngắn (0,7 giây). Bật lại ở Settings, Accessibility, Visual effects để có hiệu ứng đầy đủ.

