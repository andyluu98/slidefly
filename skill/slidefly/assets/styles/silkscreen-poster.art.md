# Poster in lụa: luật vẽ minh họa SVG cho từng slide

Dùng cùng `silkscreen-poster.css`. Lớp sân khấu đã dựng sẵn tờ poster (trời bậc thang, mặt trời vòng tròn, ba lớp núi, cây thông, dải thông tin tối). File này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, như một bản in khác kéo lên cùng tờ giấy. Deck mẫu: `gallery/73_demo-silkscreen-poster.html`.

## 1. Tinh thần
- **Mỗi màu là một lớp mực đặc, kéo qua lưới một lần.** Mực sau phủ kín mực trước. Mép hình là chỗ một lớp mực dừng lại, không có nét viền, không có chấm tram.
- **Không có gradient.** Bầu trời, sương mù, độ sâu đều là **dải màu bậc thang**: một màu phẳng, các vạch mỏng dần, rồi màu kế tiếp. Xa thì nhạt, gần thì đậm; chiều sâu nằm ở độ đậm, không bao giờ nằm ở độ mờ.
- **Giấy là một màu.** Chỗ không in là chỗ sáng nhất của tờ giấy (ánh nắng, vệt sáng, khoảng trắng của nước).
- **Màu nhấn hiếm.** Cam đỏ chỉ dành cho mặt trời, đường đi duy nhất (chấm tròn nối chấm) và con số quan trọng nhất của slide.
- Hình kể bằng cảnh: núi, thông, đường mòn, tấm poster nhỏ. Thông tin (tên, con số) nằm ở dải tối cuối tờ hoặc ở chữ slide, không nhét vào hình.
- Khác `risograph` (mực trong, chồng màu, tram chấm, lệch đăng mạnh) và `bold-poster` (chữ khổng lồ): ở đây mực đặc, phẳng, không tram, chỉ lệch đăng 2 đến 3 px.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Lớp CSS trong deck | Giá trị |
|---|---|---|
| Giấy kem | `ss-paper` (thẻ: `ss-card`) | #F4E9D0 (thẻ #FBF3DF) |
| Trời sáng | `ss-s1` | #F6CD98 |
| Trời đậm, vạch | `ss-s2` | #EE9A73 |
| Núi xa, mặt sáng núi xa | `ss-far`, `ss-farl` | #9A7FA8, #B99BC0 |
| Đồi giữa, mặt sáng | `ss-mid`, `ss-midl` | #3E7079, #5E9096 |
| Gần nhất, dải thông tin | `ss-near` | #1E3B3F |
| Màu nhấn (hiếm) | `ss-acc` | #E8553D |
| Bóng lệch đăng | `ss-ghost` | #7A2616, độ mờ 42% |

- **Tối đa 6 mực** cho một hình: trời sáng, trời đậm, xa, giữa, gần, nhấn. Giấy kem là màu thứ bảy.
- Tô màu bằng **class trong khối `<style>` của deck** (`class="ss-acc"`), không ghi `fill="var(...)"` trong thuộc tính: PPTX chỉ đọc màu từ class.
- **Không viền.** Hình chỉ có `fill`. Nét (`stroke`) chỉ dành cho: vòng tròn mặt trời, đường chấm, đường dóng mảnh, vạch giả chữ trên nền tối.
- **Lệch đăng:** bản in sau lệch (+3, +3) px so với bản trước; mặt trời có bóng ma `ss-ghost` lệch (3, 3); thẻ poster có bóng ma lệch (6, 6) làm mép dày. Lệch cố định, không rung.
- **Mặt sáng:** núi xa có mặt sáng hình tam giác lởm chởm ở sườn trái đỉnh; đồi giữa có mép sáng trên trái, làm bằng cách in đồi sáng rồi in đồi tối lệch (14, 12).
- **Bậc thang trời:** khối đậm (khoảng 25% chiều cao), rồi vạch sáng và vạch đậm xen kẽ mỏng dần (bề dày 7, 11, 15, 20, 26, 33 cho vạch sáng; 20, 14, 10, 7, 5, 3 cho vạch đậm), cuối là giấy trắng.
- **Chữ trong hình:** chữ tiếng Việt dùng `var(--font-display)` (Big Shoulders Display 800, IN HOA, giãn 0,1em), 21 đến 25px; số trong huy hiệu tròn màu giấy, chữ #1E3B3F.
- Mọi `id` (clipPath, pattern) trong SVG phải duy nhất trong cả deck, ví dụ `ssc1`, `sst2`.

## 3. Hình mẫu lặp lại
**Mặt trời vòng tròn** (lõi đặc, bốn vòng mảnh dần; bóng ma lệch (3, 3) vẽ trước):
```svg
<circle class="ss-acc" cx="0" cy="0" r="12"/>
<circle class="ss-ring" r="19" stroke-width="3.4"/><circle class="ss-ring" r="26" stroke-width="2.6"/><circle class="ss-ring" r="32" stroke-width="1.8"/>
```
**Thẻ poster nhỏ** (một slide thu nhỏ: bóng ma, viền kem, trời bậc thang, mặt trời, núi xa, đất tối; cắt bằng `clipPath`):
```svg
<rect class="ss-ghost" x="-112" y="-64" width="236" height="138"/><rect class="ss-card" x="-118" y="-69" width="236" height="138"/>
<clipPath id="sst1"><rect x="-110" y="-61" width="220" height="122"/></clipPath>
<g clip-path="url(#sst1)"><rect class="ss-s1" .../><rect class="ss-s2" .../><path class="ss-far" d="..."/><path class="ss-near" d="..."/></g>
```
**Đường đi in từng chấm** (đường duy nhất của hình; đầu mũi tên là tam giác đặc):
```svg
<path class="ss-routeN" d="M70 600C170 560 190 470 290 420S470 360 520 250"/><path class="ss-near" d="M660 62l-34 4 14 24z"/>
```
`.ss-routeN` nét 7px, `stroke-dasharray: 0 17`, đầu nét tròn; trên nền tối dùng `ss-route` (cam đỏ) hoặc `ss-routeL` (trời sáng).
**Huy hiệu số** (nối hình với bảng chú giải): `<circle class="ss-paper" r="19"/><text class="ss-num" text-anchor="middle">1</text>`.
**Dải thử mực** (6 ô vuông 44x22, mỗi ô một mực) dưới đáy hình hoặc dưới bảng chú giải; **dấu căn đăng** (vòng tròn và chữ thập) ở góc.
**Vạch giả chữ** trên nền tối: `<path class="ss-bar" d="M158 392H300M312 392H352"/>` (nét 7px, màu kem), dùng khi không cần chữ thật.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm bên trái (x 120 đến 1040). Tờ poster của style chiếm x 1080 đến 1820, y 80 đến 990: trời y 80 đến 800, mặt trời tâm (1450, 400), núi từ y 470, dải tối y 800 đến 990. SVG đặt `left:1100px; top:110px; width:700; height:690`, **vẽ chồng lên vùng trời**: ba thẻ poster nhỏ (rộng 124, 168, 222, nghiêng -14, -8, 5 độ) nhảy dọc một đường chấm từ chân núi lên góc trời (deck mẫu: slide "bay" qua các bước). Thẻ nào cũng tự mang trời bậc thang, mặt trời, núi. Đường chấm kết thúc bằng mũi tên đặc; điểm xuất phát là chấm cam đỏ có lõi giấy.
- Lớp vẽ: đường chấm, thẻ nhỏ nhất, thẻ giữa, thẻ lớn (xa tới gần, mỗi thẻ che một phần thẻ trước), chấm xuất phát.
- Không vẽ vào dải tối cuối poster (y 800 đến 990).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content` là **tấm thẻ tối** x 1240 đến 1840, y 230 (hoặc 250) đến 1010; phần đầu thẻ (y đến khoảng 380) đã có vạch giả chữ của dải thông tin. SVG đặt `left:1260px; top:390px; width:540; height:590`, vẽ bằng mực sáng trên nền tối. Chừa dải **y 590 đến 672** (tọa độ cục bộ 200 đến 282) cho `hl-text` (PPTX căn giữa chữ này theo chiều dọc). Nửa trên: một vật, hai tư thế (mặt trời nhỏ thấp bên trái, mặt trời lớn cao bên phải, hai vòng mờ trung gian `ss-pale`, đường chấm nối, cùng huy hiệu số 1). Nửa dưới: bảng "mực in" gồm ba hàng: huy hiệu số, ô mực, vạch giả chữ.
- Một thành phần = một vật hoặc một tư thế; cùng một vật thì cùng số.

**c. Quy trình hoặc dòng thời gian.** Diễn viên `band` là trục (y 622 đến 638). SVG đặt chồng lên trục y 630 của `timeline`: `left:120px; top:560px; width:1680; height:140`. Mỗi bước một **trạm** tại x = 16 + i × 342,4 (5 bước), y cục bộ 70: vầng giấy bán kính 31 che trục, đĩa tối 22, vòng giấy 12, lõi cam đỏ 7. Trạm cuối là **mặt trời** (lõi và ba vòng) vì đó là đích. Giữa hai trạm là cung chấm cam đỏ cao tối đa 28px kèm mũi tên nhỏ. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải y 836 đến 986 dưới mỗi con số: `left:120px; top:836px; width:1680; height:150`, tâm cột cục bộ x 264, 840, 1416. Mỗi cột một thẻ poster 236x138 có **số vạch bằng số ý** (3, 5, 7): nhiều ý thì vạch mỏng đi. Cột "nên tách slide" thêm đường cắt đứt nét cam đỏ chạy dọc giữa thẻ và hai cạnh ngang nhỏ ở hai đầu. So sánh hai phương án: hai thẻ cạnh nhau cùng cỡ, cùng bảng mực.

## 5. Chuyển động và xuất PPTX
- Mỗi lớp mực **hiện bằng một nhịp**: bọc `<g class="reveal">` (hiện dần, trượt nhẹ). Thứ tự in: đường đi, hình xa, hình gần, huy hiệu số, chữ. Không có fade riêng lẻ từng nét.
- **Không gắn `draw` vào đường chấm** (`draw` ghi đè `stroke-dasharray`). Chỉ dùng `draw pathLength="1"` cho nét liền, ví dụ vạch mảnh dài; hình tô đặc không cần `draw`.
- Không dùng animation lặp, không đổi màu, không rung lắc. Cả hình xong trong khoảng 2 giây.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng thuộc tính `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.ss-acc`). SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn trong SVG, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không lệch khỏi tờ poster, trục và thẻ tối của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ có sáu mực của bảng màu cùng giấy kem và màu nhấn đúng một vật; không gradient, không viền quanh hình đặc.
- Rà đường chấm: không có `draw` trên nét đứt; mọi `id` duy nhất.

## 6. Cấm
- Gradient, nét viền quanh hình đặc, chấm tram, bóng đổ mờ, glow, render 3D. Chiều sâu chỉ bằng độ đậm các lớp mực.
- Màu ngoài bảng. Quá 6 mực trong một hình. Dùng màu nhấn cho nhiều vật cùng lúc.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165, vào dải `hl-text` (y 590 đến 672 của slide `content`) hay trục timeline.
- Ghi số liệu bịa trong hình (số vạch của thẻ chỉ minh họa "càng nhiều ý càng mảnh"; không ghi số đo, giá, ngày giả). Dùng chữ ký hiệu hoặc nhãn "VÍ DỤ".
- Sao chép poster, tên công viên, logo, tên cơ quan có thật. Người vẽ thay cho cảnh; chữ dài trong SVG.

Phỏng theo lemo-opuscar `styles/silkscreen-poster/STYLE.md` (MIT) qua MotionFly.
