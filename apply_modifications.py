#!/usr/bin/env python3
"""
Apply all modifications to Arabic HTML
"""

# Read the current Arabic HTML
with open('/home/ubuntu/SES-Website/index-ar.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("=== STARTING MODIFICATIONS ===\n")
print(f"Original: {len(content)} characters, {content.count(chr(10))} lines\n")

# ========== MODIFICATION 1: Extract Mission & Vision section ==========
mission_start = content.find('<!-- Mission & Vision Section -->')
mission_end = content.find('</section>', mission_start) + len('</section>')
mission_section = content[mission_start:mission_end]

# Remove it from current position
content_before_mission = content[:mission_start]
content_after_mission = content[mission_end+1:]  # +1 for newline
content = content_before_mission + content_after_mission

print("✅ Step 1: Removed Mission & Vision section from current position")
print(f"   New length: {len(content)} characters\n")

# ========== MODIFICATION 2: Insert "What We Offer" section ==========
vision_banner_end = content.find('</div>\n    </div>\n    \n    <!-- Solutions Section -->')
if vision_banner_end == -1:
    print("ERROR: Could not find insertion point")
    exit(1)

insertion_point = content.find('</div>\n    \n    <!-- Solutions Section -->', vision_banner_end)

what_we_offer = '''
    <!-- Value Proposition - What We Offer -->
    <section id="about">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">ما نقدمه</h2>
            <p class="section-subtitle" data-aos="fade-up" data-aos-delay="200">
                إدارة بيئية شاملة لموقع واحد أو آلاف المواقع - منصة تقنية متكاملة تربط الحكومات والشركات والمجتمعات
            </p>
            
            <div class="values-grid">
                <div class="value-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="value-icon">
                        <i class="fas fa-layer-group"></i>
                    </div>
                    <h3>منصة متكاملة</h3>
                    <p>منظومة كاملة من جمع النفايات إلى ذكاء الاقتصاد الدائري، متصلة بسلاسة</p>
                </div>
                
                <div class="value-card" data-aos="fade-up" data-aos-delay="200">
                    <div class="value-icon">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h3>رؤية كاملة</h3>
                    <p>تتبع ومراقبة وتحليلات فورية عبر جميع العمليات البيئية</p>
                </div>
                
                <div class="value-card" data-aos="fade-up" data-aos-delay="300">
                    <div class="value-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>امتثال كامل</h3>
                    <p>توافق تنظيمي بنسبة 100٪ مع مسارات تدقيق آلية وتقارير شفافة</p>
                </div>
            </div>
        </div>
    </section>
'''

content = content[:insertion_point] + what_we_offer + '\n    ' + content[insertion_point:]

print("✅ Step 2: Inserted 'What We Offer' section")
print(f"   New length: {len(content)} characters\n")

# ========== MODIFICATION 3: Add missing stakeholder cards ==========
# Find the last solution card (Communities)
last_card_end = content.rfind('</div>\n                </div>\n            </div>\n        </div>\n    </section>\n    \n    <!-- Stats Section -->')

if last_card_end == -1:
    print("ERROR: Could not find Solutions section end")
    exit(1)

# Find the proper insertion point (before the closing divs)
insertion_point_cards = content.rfind('</div>\n                \n                <div class="solution-card"', 0, last_card_end)
if insertion_point_cards == -1:
    # Try alternative pattern
    insertion_point_cards = content.rfind('</ul>\n                </div>', 0, last_card_end)
    insertion_point_cards = content.find('</div>', insertion_point_cards) + len('</div>')

new_cards = '''
                
                <div class="solution-card" data-aos="fade-up" data-aos-delay="400">
                    <div class="solution-icon">
                        <i class="fas fa-recycle"></i>
                    </div>
                    <h3>مرافق إدارة النفايات</h3>
                    <h4>بسّط العمليات وعظّم الكفاءة</h4>
                    <p>تبسيط العمليات وتحسين الكفاءة مع سير العمل الرقمي</p>
                    <ul class="solution-benefits">
                        <li>التتبع والتحقق الآلي</li>
                        <li>تصنيف المواد</li>
                        <li>إدارة السعة</li>
                        <li>توثيق الامتثال</li>
                    </ul>
                </div>
                
                <div class="solution-card" data-aos="fade-up" data-aos-delay="500">
                    <div class="solution-icon">
                        <i class="fas fa-leaf"></i>
                    </div>
                    <h3>شركاء الاقتصاد الدائري</h3>
                    <h4>تمكين استعادة المواد المستدامة</h4>
                    <p>دعم التنمية الحضرية المستدامة وحماية الصحة العامة</p>
                    <ul class="solution-benefits">
                        <li>سوق إعادة التدوير</li>
                        <li>مطابقة المواد</li>
                        <li>تتبع الجودة</li>
                        <li>تكامل سلسلة التوريد</li>
                    </ul>
                </div>'''

content = content[:insertion_point_cards] + new_cards + '\n            ' + content[insertion_point_cards:]

print("✅ Step 3: Added 2 new stakeholder cards (Waste Facilities & Circular Economy)")
print(f"   New length: {len(content)} characters\n")

# ========== MODIFICATION 4: Re-insert Mission & Vision as "Guiding Principles" ==========
# Find the Stats section start
stats_section_start = content.find('<!-- Stats Section -->')
if stats_section_start == -1:
    print("ERROR: Could not find Stats section")
    exit(1)

# Modify the mission section to be "Guiding Principles"
guiding_principles = mission_section.replace(
    '<!-- Mission & Vision Section -->',
    '<!-- Guiding Principles Section -->'
).replace(
    '<h2 class="section-title" data-aos="fade-up">رسالتنا</h2>',
    '<h2 class="section-title" data-aos="fade-up">المبادئ التوجيهية</h2>'
).replace(
    'نمكّن الحكومات والشركات من الوفاء بمسؤولياتها البيئية بكفاءة من خلال الأتمتة الذكية التي تبسط الامتثال، وتحسن المساءلة، وتدعم النمو المستدام.',
    'القيم التي تدفع مهمتنا لبناء مستقبل مستدام للمملكة العربية السعودية'
)

# Insert before Stats section
content = content[:stats_section_start] + guiding_principles + '\n    \n    ' + content[stats_section_start:]

print("✅ Step 4: Re-inserted as 'Guiding Principles' section")
print(f"   Final length: {len(content)} characters\n")

# ========== SAVE MODIFIED FILE ==========
with open('/home/ubuntu/SES-Website/index-ar-modified.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("=== MODIFICATIONS COMPLETE ===")
print(f"\nOriginal: 31469 characters, 922 lines")
print(f"Modified: {len(content)} characters, {content.count(chr(10))} lines")
print(f"Difference: +{len(content) - 31469} characters, +{content.count(chr(10)) - 922} lines")
print("\n✅ Saved to: index-ar-modified.html")

