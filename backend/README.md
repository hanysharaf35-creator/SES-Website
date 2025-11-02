# SES Website CMS Backend

Complete Content Management System for Smart Environmental Solution website.

## 🎯 Project Overview

This backend CMS allows non-technical users to manage all website content without coding:
- Pages and sections
- Sectors and core values
- Statistics and case studies
- YouTube videos
- Blog posts
- Demo requests
- Media library
- Site settings

## 🔧 Technology Stack

- **Backend:** PHP 8.1+
- **Database:** MySQL 8.0+
- **Authentication:** Session-based with bcrypt
- **Frontend (Admin):** HTML5, CSS3, JavaScript, Bootstrap 5
- **Rich Text Editor:** TinyMCE
- **Icons:** Font Awesome

## 📁 Project Structure

```
backend/
├── admin/              # Admin panel interface
├── api/                # API endpoints
├── config/             # Configuration files
├── database/           # Database schema and migrations
│   ├── schema.sql      # Database structure
│   └── sample_data.sql # Initial content
├── includes/           # PHP includes and classes
└── uploads/            # User uploaded files
    ├── images/
    ├── videos/
    └── documents/
```

## 📊 Database Schema

**15 Tables:**
1. users - Admin users
2. settings - Site configuration
3. pages - Page content
4. page_sections - Section content
5. sectors - Solutions sectors
6. core_values - Company values
7. statistics - Impact numbers
8. case_studies - Success stories
9. video_categories - Video categories
10. videos - YouTube videos
11. blog_categories - Blog categories
12. blog_posts - Blog articles
13. demo_requests - Form submissions
14. media - Media library
15. sessions - User sessions

## 🚀 Installation

### Prerequisites
- PHP 8.1 or higher
- MySQL 8.0 or higher
- Apache/Nginx web server
- cPanel hosting (for production)

### Steps

1. **Create MySQL Database**
   ```sql
   CREATE DATABASE ses_website CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Import Database Schema**
   ```bash
   mysql -u username -p ses_website < database/schema.sql
   ```

3. **Import Sample Data**
   ```bash
   mysql -u username -p ses_website < database/sample_data.sql
   ```

4. **Configure Database Connection**
   - Copy `config/config.example.php` to `config/config.php`
   - Update database credentials

5. **Set Permissions**
   ```bash
   chmod 755 uploads/
   chmod 755 uploads/images/
   chmod 755 uploads/videos/
   chmod 755 uploads/documents/
   ```

6. **Access Admin Panel**
   - URL: `https://yourdomain.com/backend/admin/`
   - Username: `admin`
   - Password: `Admin@123`
   - **IMPORTANT:** Change password immediately after first login!

## 🔒 Security Features

- SQL injection prevention (PDO prepared statements)
- XSS protection (input sanitization)
- CSRF tokens on all forms
- bcrypt password hashing
- Role-based access control
- Session security
- File upload validation

## 👥 User Roles

- **Super Admin:** Full access to all features
- **Editor:** Can manage content, cannot manage users/settings
- **Viewer:** Read-only access

## 📝 Default Admin Credentials

**Username:** admin  
**Password:** Admin@123  
**⚠️ MUST be changed after first login!**

## 🛠️ Development Status

**Phase 1: Database Design** ✅ Complete
- Schema created
- Sample data added
- 15 tables with relationships

**Phase 2: Authentication** ⏳ In Progress
- Login system
- Session management
- Role-based access

**Phase 3: Admin Panel** ⏳ Planned
- Dashboard
- Content management
- Media center
- Settings

**Phase 4: Frontend Integration** ⏳ Planned
- Dynamic PHP pages
- Language switching
- Form handling

**Phase 5: Testing & Deployment** ⏳ Planned
- Security testing
- Performance optimization
- Documentation

## 📚 Documentation

- Installation Guide: `docs/INSTALLATION.md` (coming soon)
- User Manual: `docs/USER_GUIDE.md` (coming soon)
- Admin Guide: `docs/ADMIN_GUIDE.md` (coming soon)
- API Documentation: `docs/API.md` (coming soon)

## 🤝 Support

For questions or issues, contact the development team.

## 📄 License

Proprietary - Smart Environmental Solution

---

**Last Updated:** November 2, 2025  
**Version:** 0.1.0-alpha  
**Status:** In Development

