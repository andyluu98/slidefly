# Vũ đạo Morph: công thức chuyển cảnh dùng lại được

Mỗi công thức = cách đặt tư thế cho một vài diễn viên ở hai layout liền nhau. Ví dụ CSS lấy từ các style có sẵn.

## 1. Vòng tròn phóng to (zoom ring): `xanh-dai-hoc`
Nhiều vòng đồng tâm, mỗi vòng phóng với tốc độ khác nhau vì kích thước đích khác nhau. Slide 1 vòng nhỏ 125px, slide 2 vòng lớn 1580px: cảm giác ống kính lao vào.
```css
.deck-stage[data-pose="dh1"] { --w-soft: 125.5px; --w-main: 125.5px; --rbw: 20px; }
.deck-stage[data-pose="dh2"] { --w-soft: 1580.6px; --w-main: 798.9px; --rbw: 160px; }
```
Mẹo: animate cả độ dày viền (`--rbw`) để vòng "nở" chứ không chỉ phóng.

## 2. Cánh gà (wings)
Diễn viên chờ ở tọa độ âm hoặc quá 1920 rồi bay vào. Thẻ xanh của mẫu Đại Học nằm ở y 1170 (dưới khung) trước khi trồi lên làm thẻ bìa.
```css
[data-actor="card"] { --y: var(--card-y); }          /* mặc định 1170px: dưới khung */
.deck-stage[data-layout="cover"] { --card-y: 80px; } /* trồi lên */
```

## 3. Khối chiếm sân khấu (takeover): `swiss-modern`
Một khối nhỏ ở slide này nở ra phủ kín màn hình ở slide sau (quote nền đen, closing nền đỏ). Nhớ đổi màu chữ theo layout:
```css
[data-layout="closing"] [data-actor="red"] { --x: 0px; --y: 0px; --w: 1920px; --h: 1080px; }
.deck-stage[data-layout="closing"] { --fg: #fff; --accent: #0a0a0a; }
```

## 4. Khối thành trục (axis morph): `swiss-modern`
Khối đỏ ở bìa (640x1080) dẹt lại thành trục thời gian (1680x8) ở timeline: người xem thấy "cùng một vật" đổi vai trò.

## 5. Thẻ phóng ra toàn màn hình: `xanh-dai-hoc`
Thẻ bìa (1659x921) phóng thành nền toàn màn hình ở agenda; đồng thời hoa 8 cánh xoay 180 độ và phóng từ 0,29 lên 1.
```css
.deck-stage[data-layout="agenda"] { --card-x: 0px; --card-y: 0px; --card-w: 1920px; --card-h: 1080px; --fs: 1; --fr: 0deg; }
```

## 6. Xoay theo parity
Hai slide `content` liền nhau: đổi `--r` 0deg sang 180deg hoặc đổi kích thước vòng ở `[data-parity="even"]` để vẫn có chuyển động mà bố cục giữ nguyên.

## 7. Khung ôm điểm nhấn
Ở `content`, đặt đĩa/khung diễn viên đúng vùng `.highlight` (x 1260..1800, tâm y 630) để icon/số nằm gọn trong hình: diễn viên vừa trang trí vừa làm khung cho thông tin.

## Nguyên tắc
- Mỗi lần chuyển, 2-4 diễn viên đổi rõ rệt là đủ; tất cả cùng đổi dễ rối.
- Diễn viên lớn nên đổi kích thước/màu, diễn viên nhỏ nên đổi vị trí.
- Không cho đường kẻ chạy xuyên qua chữ; khối tràn nền thì đổi màu chữ cùng lúc.
- Thời lượng mặc định 1,2 giây (`--morph-dur`). Deck dày chữ có thể đặt `:root { --morph-dur: 0.9s; }` trong `<style>` của deck.
