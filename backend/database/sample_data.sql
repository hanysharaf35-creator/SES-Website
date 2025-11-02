-- SES Website CMS Sample Data
-- This file populates the database with initial content

-- Insert default admin user
-- Username: admin
-- Password: Admin@123 (MUST be changed after first login)
INSERT INTO users (username, email, password_hash, role, status) VALUES
('admin', 'admin@smartenvironmentalsolution.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'super_admin', 'active');

-- Insert default settings
INSERT INTO settings (setting_key, setting_value, setting_type, setting_group) VALUES
('site_title_en', 'Smart Environmental Solution', 'text', 'general'),
('site_title_ar', 'الحلول البيئية الذكية', 'text', 'general'),
('site_tagline_en', 'Intelligent Solutions for Sustainable Cities', 'text', 'general'),
('site_tagline_ar', 'حلول ذكية للمدن المستدامة', 'text', 'general'),
('contact_email', 'info@smartenvironmentalsolution.com', 'text', 'contact'),
('contact_phone', '+966 XX XXX XXXX', 'text', 'contact'),
('primary_color', '#1e3a52', 'color', 'appearance'),
('secondary_color', '#5bc0de', 'color', 'appearance'),
('accent_color', '#f97316', 'color', 'appearance'),
('videos_per_page', '6', 'number', 'media'),
('blog_posts_per_page', '3', 'number', 'media');

-- Insert pages
INSERT INTO pages (slug, title_en, title_ar, meta_desc_en, meta_desc_ar, hero_title_en, hero_title_ar, hero_subtitle_en, hero_subtitle_ar, status) VALUES
('home', 'Home', 'الرئيسية', 'Smart Environmental Solution - Building Saudi Arabia''s Sustainable Future', 'الحلول البيئية الذكية - بناء مستقبل المملكة المستدام', 'Building Saudi Arabia''s Sustainable Future', 'بناء مستقبل المملكة المستدام', 'Transforming environmental compliance into competitive advantage through intelligent automation', 'تحويل الامتثال البيئي إلى ميزة تنافسية من خلال الأتمتة الذكية', 'published'),
('about', 'About Us', 'من نحن', 'Learn about Smart Environmental Solution', 'تعرف على الحلول البيئية الذكية', 'About Smart Environmental Solution', 'عن الحلول البيئية الذكية', 'Our mission, vision, and values', 'مهمتنا ورؤيتنا وقيمنا', 'published'),
('solutions', 'Solutions', 'الحلول', 'Our solutions for sustainable environmental management', 'حلولنا للإدارة البيئية المستدامة', 'Comprehensive Environmental Solutions', 'حلول بيئية شاملة', 'Tailored for every stakeholder', 'مصممة لكل أصحاب المصلحة', 'published'),
('impact', 'Impact', 'التأثير', 'Measurable results and success stories', 'نتائج قابلة للقياس وقصص نجاح', 'Real Results, Real Impact', 'نتائج حقيقية، تأثير حقيقي', 'Transforming environmental compliance across Saudi Arabia', 'تحويل الامتثال البيئي في جميع أنحاء المملكة', 'published'),
('media', 'Media Center', 'المركز الإعلامي', 'Videos, news, and updates', 'فيديوهات وأخبار وتحديثات', 'Media Center', 'المركز الإعلامي', 'Latest videos, news, and updates', 'أحدث الفيديوهات والأخبار والتحديثات', 'published'),
('contact', 'Contact Us', 'اتصل بنا', 'Get in touch with Smart Environmental Solution', 'تواصل مع الحلول البيئية الذكية', 'Get In Touch', 'تواصل معنا', 'Request a demo or contact our team', 'اطلب عرضًا توضيحيًا أو تواصل مع فريقنا', 'published');

-- Insert sectors
INSERT INTO sectors (title_en, title_ar, description_en, description_ar, icon, features_en, features_ar, sector_order, visible) VALUES
('Government & Municipalities', 'الحكومة والبلديات', 'Transform compliance into competitive advantage', 'تحويل الامتثال إلى ميزة تنافسية', 'fa-landmark', '["Digital permit processing", "Real-time compliance monitoring", "Automated reporting", "Violation tracking"]', '["معالجة التصاريح الرقمية", "مراقبة الامتثال في الوقت الفعلي", "إعداد التقارير الآلية", "تتبع المخالفات"]', 1, TRUE),
('Contractors & Developers', 'المقاولون والمطورون', 'Navigate compliance with confidence', 'التنقل في الامتثال بثقة', 'fa-hard-hat', '["Project compliance tracking", "Document management", "Automated notifications", "Audit trail"]', '["تتبع امتثال المشروع", "إدارة المستندات", "الإخطارات الآلية", "سجل التدقيق"]', 2, TRUE),
('Service Companies', 'شركات الخدمات', 'Optimize operations and win more business', 'تحسين العمليات والفوز بمزيد من الأعمال', 'fa-truck', '["Fleet management", "Route optimization", "Performance analytics", "Customer portal"]', '["إدارة الأسطول", "تحسين المسار", "تحليلات الأداء", "بوابة العملاء"]', 3, TRUE),
('Waste Management Facilities', 'مرافق إدارة النفايات', 'Streamline operations and compliance', 'تبسيط العمليات والامتثال', 'fa-recycle', '["Intake tracking", "Material classification", "Compliance reporting", "Capacity management"]', '["تتبع الاستلام", "تصنيف المواد", "تقارير الامتثال", "إدارة السعة"]', 4, TRUE),
('Circular Economy Partners', 'شركاء الاقتصاد الدائري', 'Connect waste streams to value opportunities', 'ربط تدفقات النفايات بفرص القيمة', 'fa-arrows-rotate', '["Material marketplace", "Quality tracking", "Supply chain integration", "Impact measurement"]', '["سوق المواد", "تتبع الجودة", "تكامل سلسلة التوريد", "قياس التأثير"]', 5, TRUE),
('Communities', 'المجتمعات', 'Build cleaner, safer neighborhoods', 'بناء أحياء أنظف وأكثر أمانًا', 'fa-users', '["Transparency portal", "Issue reporting", "Progress tracking", "Educational resources"]', '["بوابة الشفافية", "الإبلاغ عن المشكلات", "تتبع التقدم", "الموارد التعليمية"]', 6, TRUE);

-- Insert core values
INSERT INTO core_values (title_en, title_ar, description_en, description_ar, icon, value_order, visible) VALUES
('Innovation First', 'الابتكار أولاً', 'Leading with cutting-edge technology to solve environmental challenges', 'الريادة بالتكنولوجيا المتطورة لحل التحديات البيئية', 'fa-lightbulb', 1, TRUE),
('Environmental Stewardship', 'الإشراف البيئي', 'Protecting our planet through responsible technology and sustainable practices', 'حماية كوكبنا من خلال التكنولوجيا المسؤولة والممارسات المستدامة', 'fa-leaf', 2, TRUE),
('Transparency & Accountability', 'الشفافية والمساءلة', 'Building trust through open, auditable systems and clear communication', 'بناء الثقة من خلال الأنظمة المفتوحة القابلة للتدقيق والتواصل الواضح', 'fa-shield-halved', 3, TRUE),
('Partnership', 'الشراكة', 'Working collaboratively with governments, businesses, and communities', 'العمل بشكل تعاوني مع الحكومات والشركات والمجتمعات', 'fa-handshake', 4, TRUE),
('Impact-Driven Excellence', 'التميز المدفوع بالتأثير', 'Measuring success by tangible outcomes and real-world impact', 'قياس النجاح من خلال النتائج الملموسة والتأثير الواقعي', 'fa-chart-line', 5, TRUE);

-- Insert statistics
INSERT INTO statistics (value, label_en, label_ar, description_en, description_ar, icon, stat_order, visible) VALUES
('40%', 'Reduction in Violations', 'تقليل المخالفات', 'Fewer compliance violations through proactive monitoring', 'عدد أقل من مخالفات الامتثال من خلال المراقبة الاستباقية', 'fa-chart-line', 1, TRUE),
('50%', 'Faster Permit Processing', 'معالجة أسرع للتصاريح', 'Streamlined digital workflows reduce processing time', 'تقليل وقت المعالجة من خلال سير العمل الرقمي المبسط', 'fa-clock', 2, TRUE),
('30%', 'Efficiency Improvement', 'تحسين الكفاءة', 'Optimized operations across the waste management sector', 'عمليات محسّنة عبر قطاع إدارة النفايات', 'fa-gauge-high', 3, TRUE),
('100%', 'Audit Trail Compliance', 'امتثال سجل التدقيق', 'Complete transparency and accountability in all operations', 'شفافية ومساءلة كاملة في جميع العمليات', 'fa-check-circle', 4, TRUE);

-- Insert case studies
INSERT INTO case_studies (title_en, title_ar, description_en, description_ar, icon, metrics_en, metrics_ar, case_order, visible) VALUES
('Municipal Transformation', 'تحول البلدية', 'A major Saudi municipality reduced permit processing time by 60% while improving compliance rates across 500+ active construction sites.', 'قامت بلدية سعودية كبرى بتقليل وقت معالجة التصاريح بنسبة 60٪ مع تحسين معدلات الامتثال في أكثر من 500 موقع بناء نشط.', 'fa-building', '["60% faster processing", "45% better compliance"]', '["معالجة أسرع بنسبة 60٪", "امتثال أفضل بنسبة 45٪"]', 1, TRUE),
('Contractor Excellence', 'تميز المقاول', 'Leading construction company streamlined operations across 50 projects, reducing administrative overhead and improving environmental compliance.', 'قامت شركة إنشاءات رائدة بتبسيط العمليات عبر 50 مشروعًا، مما قلل من التكاليف الإدارية وحسّن الامتثال البيئي.', 'fa-helmet-safety', '["35% less admin time", "100% compliance rate"]', '["وقت إداري أقل بنسبة 35٪", "معدل امتثال 100٪"]', 2, TRUE),
('Service Optimization', 'تحسين الخدمة', 'Waste management company optimized fleet operations, reducing fuel costs and improving service delivery across Riyadh.', 'قامت شركة إدارة النفايات بتحسين عمليات الأسطول، مما قلل من تكاليف الوقود وحسّن تقديم الخدمة في جميع أنحاء الرياض.', 'fa-truck-fast', '["25% fuel savings", "40% more efficient routes"]', '["توفير في الوقود بنسبة 25٪", "مسارات أكثر كفاءة بنسبة 40٪"]', 3, TRUE);

-- Insert video categories
INSERT INTO video_categories (name_en, name_ar, slug, category_order) VALUES
('Projects', 'المشاريع', 'projects', 1),
('Exhibitions', 'المعارض', 'exhibitions', 2),
('Tutorials', 'الدروس التعليمية', 'tutorials', 3),
('News', 'الأخبار', 'news', 4);

-- Insert sample videos (placeholder YouTube IDs)
INSERT INTO videos (youtube_id, title_en, title_ar, description_en, description_ar, thumbnail_url, category_id, video_order, visible) VALUES
('dQw4w9WgXcQ', 'SESDRAS Platform Overview', 'نظرة عامة على منصة SESDRAS', 'Comprehensive overview of the SESDRAS container management platform', 'نظرة شاملة على منصة إدارة الحاويات SESDRAS', 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', 1, 1, TRUE),
('dQw4w9WgXcQ', 'Smart City Exhibition 2024', 'معرض المدن الذكية 2024', 'Our participation in the Smart City Exhibition in Riyadh', 'مشاركتنا في معرض المدن الذكية في الرياض', 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', 2, 2, TRUE),
('dQw4w9WgXcQ', 'How to Request a Container', 'كيفية طلب حاوية', 'Step-by-step tutorial on requesting a waste container', 'دليل خطوة بخطوة لطلب حاوية نفايات', 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', 3, 3, TRUE);

-- Insert blog categories
INSERT INTO blog_categories (name_en, name_ar, slug, category_order) VALUES
('Company News', 'أخبار الشركة', 'company-news', 1),
('Industry Insights', 'رؤى الصناعة', 'industry-insights', 2),
('Case Studies', 'دراسات الحالة', 'case-studies', 3),
('Sustainability', 'الاستدامة', 'sustainability', 4);

-- Insert sample blog posts
INSERT INTO blog_posts (title_en, title_ar, slug, excerpt_en, excerpt_ar, content_en, content_ar, category_id, author_id, published_at, status) VALUES
('Launching SESDRAS: A New Era in Waste Management', 'إطلاق SESDRAS: عصر جديد في إدارة النفايات', 'launching-sesdras-new-era-waste-management', 'We are excited to announce the launch of SESDRAS, our comprehensive container waste management platform.', 'يسعدنا الإعلان عن إطلاق SESDRAS، منصتنا الشاملة لإدارة نفايات الحاويات.', '<p>We are excited to announce the launch of SESDRAS, our comprehensive container waste management platform designed specifically for the Saudi market.</p><p>SESDRAS represents a significant step forward in environmental compliance and waste management efficiency...</p>', '<p>يسعدنا الإعلان عن إطلاق SESDRAS، منصتنا الشاملة لإدارة نفايات الحاويات المصممة خصيصًا للسوق السعودي.</p><p>يمثل SESDRAS خطوة كبيرة إلى الأمام في الامتثال البيئي وكفاءة إدارة النفايات...</p>', 1, 1, NOW(), 'published'),
('Vision 2030 and Environmental Sustainability', 'رؤية 2030 والاستدامة البيئية', 'vision-2030-environmental-sustainability', 'How Smart Environmental Solution aligns with Saudi Vision 2030 goals for a sustainable future.', 'كيف تتماشى الحلول البيئية الذكية مع أهداف رؤية السعودية 2030 لمستقبل مستدام.', '<p>Saudi Vision 2030 places environmental sustainability at the heart of the Kingdom''s transformation...</p>', '<p>تضع رؤية السعودية 2030 الاستدامة البيئية في قلب تحول المملكة...</p>', 4, 1, NOW(), 'published'),
('The Future of Circular Economy in Saudi Arabia', 'مستقبل الاقتصاد الدائري في المملكة', 'future-circular-economy-saudi-arabia', 'Exploring opportunities and challenges in building a circular economy ecosystem in the Kingdom.', 'استكشاف الفرص والتحديات في بناء نظام الاقتصاد الدائري في المملكة.', '<p>The circular economy represents a paradigm shift from the traditional linear "take-make-dispose" model...</p>', '<p>يمثل الاقتصاد الدائري تحولًا نموذجيًا من النموذج الخطي التقليدي "خذ-اصنع-تخلص"...</p>', 2, 1, NOW(), 'published');

