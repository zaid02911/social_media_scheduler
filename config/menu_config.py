# config/menu_options.py
# ==================== MAIN MENU ====================
MAIN_MENU_OPTIONS = [
    "📝 CREATE & MANAGE POSTS",
    "⏰ SCHEDULE & QUEUE MANAGEMENT",
    "🔗 PLATFORM & ACCOUNT SETTINGS",
    "📊 ANALYTICS & REPORTS",
    "⚙️ SETTINGS & CONFIGURATION",
    "🆘 HELP & DOCUMENTATION",
    "🚪 EXIT"
]

# ==================== POST MANAGEMENT ====================
POST_MENU_OPTIONS = [
    "✏️ CREATE NEW POST",
    "👁️ VIEW/EDIT EXISTING POSTS",
    "📁 BULK IMPORT FROM CSV/EXCEL",
    "🗑️ DELETE POSTS",
    "↩️ BACK TO MAIN MENU"
]

# ==================== SCHEDULE MANAGEMENT ====================
SCHEDULE_MENU_OPTIONS = [
    "📅 VIEW SCHEDULED POSTS",
    "🕐 SCHEDULE NEW POST",
    "🔄 EDIT SCHEDULE",
    "⏸️ PAUSE/RESUME SCHEDULES",
    "🚫 CANCEL SCHEDULED POST",
    "⚡ POST NOW (IMMEDIATELY)",
    "📋 QUEUE STATUS & METRICS",
    "↩️ BACK TO MAIN MENU"
]

# ==================== PLATFORM MANAGEMENT ====================
PLATFORM_MENU_OPTIONS = [
    "🐦 TWITTER/X SETTINGS",
    "💼 LINKEDIN SETTINGS",
    "🐘 MASTODON SETTINGS",
    "✅ TEST PLATFORM CONNECTIONS",
    "🔑 MANAGE API CREDENTIALS",
    "⚠️ VIEW CONNECTION STATUS",
    "↩️ BACK TO MAIN MENU"
]

# ==================== ANALYTICS DASHBOARD ====================
ANALYTICS_MENU_OPTIONS = [
    "📈 POSTING STATISTICS",
    "✅ SUCCESS RATE & ERRORS",
    "🏆 BEST PERFORMING POSTS",
    "⏱️ SCHEDULE PERFORMANCE",
    "📄 GENERATE REPORT (PDF/CSV)",
    "📊 PLATFORM COMPARISON",
    "↩️ BACK TO MAIN MENU"
]

# ==================== SETTINGS MENU ====================
SETTINGS_MENU_OPTIONS = [
    "🌍 TIMEZONE & LOCALE SETTINGS",
    "🔔 NOTIFICATION PREFERENCES",
    "⏱️ SCHEDULING OPTIONS",
    "🛡️ SECURITY SETTINGS",
    "💾 DATABASE MANAGEMENT",
    "📝 LOGGING CONFIGURATION",
    "🔄 UPDATE & MAINTENANCE",
    "↩️ BACK TO MAIN MENU"
]

# ==================== HELP MENU ====================
HELP_MENU_OPTIONS = [
    "📖 GETTING STARTED GUIDE",
    "🔑 HOW TO GET API KEYS",
    "💡 TIPS & BEST PRACTICES",
    "⚠️ TROUBLESHOOTING",
    "📞 CONTACT SUPPORT",
    "ℹ️ ABOUT & VERSION INFO",
    "↩️ BACK TO MAIN MENU"
]

# ==================== POST CREATION WIZARD STEPS ====================
POST_CREATION_STEPS = [
    "✏️ CREATE NEW POST - Step 1: CONTENT",
    "✏️ CREATE NEW POST - Step 2: MEDIA",
    "✏️ CREATE NEW POST - Step 3: PLATFORMS",
    "✏️ CREATE NEW POST - Step 4: SCHEDULE"
]

# ==================== TIMEZONE OPTIONS ====================
TIMEZONE_OPTIONS = [
    "America/New_York (GMT-5)",
    "Europe/London (GMT+0)",
    "Europe/Paris (GMT+1)",
    "Asia/Dubai (GMT+4)",
    "Asia/Tokyo (GMT+9)",
    "Australia/Sydney (GMT+11)"
]

# ==================== TABLE HEADERS ====================
TABLE_HEADERS = {
    "scheduled_posts": ["ID", "Time", "Platform", "Status", "Content"],
    "post_history": ["ID", "Posted At", "Platform", "Status", "Content", "Engagement"],
    "platform_stats": ["Platform", "Posts", "Success", "Failed", "Rate"],
    "error_log": ["Timestamp", "Type", "Platform", "Message", "Resolution"]
}

# ==================== STATUS ICONS ====================
STATUS_ICONS = {
    "connected": "✅",
    "warning": "⚠️",
    "disconnected": "❌",
    "pending": "⏳",
    "success": "✅",
    "error": "❌"
}

BOX_CHARS = {
    'tl': '╔',  # top-left
    'tr': '╗',  # top-right
    'bl': '╚',  # bottom-left
    'br': '╝',  # bottom-right
    'h': '═',   # horizontal
    'v': '║',   # vertical
    'ml': '╠',  # middle-left (with divider)
    'mr': '╣',  # middle-right (with divider)
}

