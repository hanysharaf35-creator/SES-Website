#!/usr/bin/env python3
"""
Systematically modify Arabic HTML to match English structure
"""
import re

# Read the current Arabic HTML
with open('/home/ubuntu/SES-Website/index-ar.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file length:", len(content), "characters")
print("Original line count:", content.count('\n'), "lines")

# Find the Vision 2030 banner end
vision_banner_end = content.find('</div>\n    </div>\n    \n    <!-- Mission & Vision Section -->')
if vision_banner_end == -1:
    print("ERROR: Could not find Vision 2030 banner end marker")
    exit(1)

vision_banner_end = content.find('</div>\n    \n    <!-- Mission & Vision Section -->', vision_banner_end)
print(f"\nFound Vision 2030 banner end at position: {vision_banner_end}")

# Prepare the new "What We Offer" section
what_we_offer_section = '''
    <!-- Value Proposition - What We Offer -->
    <section id="about" class="section section-light">
        <div class="container">
            <div class="section-header">
                <div class="section-tag">ما نقدمه</div>
                <h2 class="section-title">إدارة بيئية شاملة<br>لموقع واحد أو آلاف المواقع</h2>
                <p class="section-subtitle">منصة تقنية متكاملة تربط الحكومات والشركات والمجتمعات في منظومات بيئية شفافة وفعالة</p>
            </div>
            
            <div class="values-grid">
                <div class="value-card">
                    <div class="value-icon">
                        <i class="fas fa-layer-group"></i>
                    </div>
                    <h3>منصة متكاملة</h3>
                    <p>منظومة كاملة من جمع النفايات إلى ذكاء الاقتصاد الدائري، متصلة بسلاسة</p>
                </div>
                
                <div class="value-card">
                    <div class="value-icon">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h3>رؤية كاملة</h3>
                    <p>تتبع ومراقبة وتحليلات فورية عبر جميع العمليات البيئية</p>
                </div>
                
                <div class="value-card">
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

print("\n✅ Step 1: Prepared 'What We Offer' section")
print(f"   Section length: {len(what_we_offer_section)} characters")

# Find the Mission & Vision section to extract and move it
mission_section_start = content.find('<!-- Mission & Vision Section -->')
mission_section_end = content.find('</section>', mission_section_start) + len('</section>')

if mission_section_start == -1 or mission_section_end == -1:
    print("ERROR: Could not find Mission & Vision section")
    exit(1)

mission_section = content[mission_section_start:mission_section_end]
print(f"\n✅ Step 2: Extracted Mission & Vision section")
print(f"   Start position: {mission_section_start}")
print(f"   End position: {mission_section_end}")
print(f"   Section length: {len(mission_section)} characters")

# Find the Solutions section
solutions_section_start = content.find('<!-- Solutions Section -->')
if solutions_section_start == -1:
    print("ERROR: Could not find Solutions section")
    exit(1)

print(f"\n✅ Step 3: Found Solutions section at position: {solutions_section_start}")

# Count current solution cards
solution_cards = content.count('<div class="solution-card"', solutions_section_start, solutions_section_start + 5000)
print(f"   Current solution cards: {solution_cards}")

print("\n✅ Ready to apply modifications")
print("\nModifications to apply:")
print("1. Insert 'What We Offer' section after Vision 2030 banner")
print("2. Remove Mission & Vision section from current position")
print("3. Expand Solutions section from 4 to 6 cards")
print("4. Re-insert Mission & Vision as 'Guiding Principles' after Solutions")

