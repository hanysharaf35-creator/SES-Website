#!/usr/bin/env python3
"""
Apply all modifications to Arabic HTML - Version 2 (Fixed)
"""

# Read the current Arabic HTML
with open('/home/ubuntu/SES-Website/index-ar.html', 'r', encoding='utf-8') as f:
    original_content = f.read()

print("=== STARTING MODIFICATIONS ===\n")
print(f"Original: {len(original_content)} characters, {original_content.count(chr(10))} lines\n")

# ========== STEP 1: Find all insertion/extraction points FIRST ==========
vision_banner_end = original_content.find('</div>\n    </div>\n    \n    <!-- Mission & Vision Section -->')
mission_start = original_content.find('<!-- Mission & Vision Section -->')
mission_end = original_content.find('</section>', mission_start) + len('</section>')
solutions_end = original_content.find('<!-- Stats Section -->')

print(f"📍 Vision Banner ends at: {vision_banner_end}")
print(f"📍 Mission section: {mission_start} to {mission_end}")
print(f"📍 Solutions section ends at: {solutions_end}\n")

# Extract mission section
mission_section = original_content[mission_start:mission_end+1]  # +1 for newline

# ========== STEP 2: Build new content in order ==========
# Part 1: Everything up to Vision Banner end
part1 = original_content[:vision_banner_end + len('</div>\n    </div>')]

# Part 2: What We Offer section (NEW)
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
    </section>'''

# Part 3: Solutions section (skip Mission section, keep Solutions)
part3_start = mission_end + 1
part3_end = original_content.find('</div>\n            </div>\n        </div>\n    </section>\n    \n    <!-- Stats Section -->')

# Find the last solution card to add new cards after it
last_card_start = original_content.rfind('<div class="solution-card"', 0, part3_end)
last_card_end = original_content.find('</div>', original_content.find('</ul>', last_card_start)) + len('</div>')

part3_before_new_cards = original_content[part3_start:last_card_end]

# New stakeholder cards
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

part3_after_new_cards = original_content[last_card_end:part3_end + len('</div>\n            </div>\n        </div>\n    </section>')]

# Part 4: Guiding Principles (modified Mission section)
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

# Part 5: Rest of the file (Stats, Why Us, Contact, Footer)
part5_start = solutions_end
part5 = original_content[part5_start:]

# ========== STEP 3: Assemble final content ==========
final_content = part1 + what_we_offer + '\n    ' + part3_before_new_cards + new_cards + part3_after_new_cards + '\n    \n    ' + guiding_principles + '\n    ' + part5

# ========== STEP 4: Save ==========
with open('/home/ubuntu/SES-Website/index-ar-modified.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("=== MODIFICATIONS COMPLETE ===\n")
print(f"Original: {len(original_content)} characters, {original_content.count(chr(10))} lines")
print(f"Modified: {len(final_content)} characters, {final_content.count(chr(10))} lines")
print(f"Difference: +{len(final_content) - len(original_content)} characters, +{final_content.count(chr(10)) - original_content.count(chr(10))} lines")
print("\n✅ Modifications applied:")
print("   1. Added 'What We Offer' section (3 value propositions)")
print("   2. Added 2 new stakeholder cards (Waste Facilities, Circular Economy)")
print("   3. Moved and renamed 'Mission' to 'Guiding Principles'")
print("\n✅ Saved to: index-ar-modified.html")

