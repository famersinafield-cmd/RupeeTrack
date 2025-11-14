# RupeeTrack - Expense Tracker App

<p align="center">A comprehensive Flutter-based mobile expense tracking application with OCR bill scanning, offline-first architecture, and beautiful data visualizations.</p>

---

## Overview

**RupeeTrack** is a feature-rich expense tracking mobile application built with Flutter that helps users manage their finances effectively. The app offers intelligent bill scanning using OCR (Optical Character Recognition), offline data persistence with Hive, and insightful analytics with interactive charts. Track your expenses, set monthly budgets, and visualize your spending patterns—all in one beautiful, intuitive interface.

---

## Key Features

### **Smart Bill Scanning**
- Capture bills using camera or gallery
- Automatic text extraction using Google ML Kit
- Extract store name, bill number, date, total amount, and itemized details
- Attach bill images to transactions for future reference

### **Offline-First Architecture**
- Local data persistence using Hive database
- Works completely offline—no internet required
- Sync pending transactions to remote server when online

### **Analytics & Visualizations**
- Interactive pie charts showing spending by category
- Bar charts for category-wise breakdown
- Monthly spending goals with progress tracking
- Visual alerts when exceeding budget limits

### **Category Management**
- Create custom expense categories
- Organize transactions by categories
- Delete categories (with option to uncategorize or delete associated transactions)
- Expandable category views with transaction lists

### **Search & Filtering**
- Search transactions by title
- Filter by category, date range, or amount
- Multiple filter combinations
- Clear and intuitive filter interface

### **Transaction Management**
- Add transactions manually or via OCR
- Edit transaction details
- Swipe-to-delete functionality
- View detailed transaction information with bill images
- Sort transactions by date (newest first)

### **Monthly Goals & Budgeting**
- Set monthly spending limits per category
- Real-time budget tracking
- Visual indicators for overspending
- Goal progress display

---

## Tech Stack

### **Frontend & Framework**
- **Flutter** - Cross-platform mobile app framework
- **Dart** - Programming language
- **Material Design 3** - UI/UX design system

### **State Management**
- **Provider** - State management solution

### **Data Persistence**
- **Hive** - Lightweight NoSQL local database
- **Hive Flutter** - Flutter integration for Hive
- Custom Hive adapters for data models

### **OCR & Image Processing**
- **Google ML Kit Text Recognition** - OCR text extraction
- **Image Picker** - Camera and gallery integration

### **Data Visualization**
- **FL Chart** - Interactive charts and graphs (Pie charts, Bar charts)

### **Backend Integration**
- **HTTP** - REST API communication
- **Multipart request** support for file uploads

### **Utilities**
- **Intl** - Date formatting and internationalization
- **JSON encoding/decoding** for structured data

---

## 📂 Project Structure

```
lib/
├── main.dart                          # Main app entry point
├── category_hive.dart                 # Category model for Hive
├── category_hive.g.dart              # Generated Hive adapter
├── transaction_item_hive.dart        # Transaction model for Hive
└── transaction_item_hive.g.dart      # Generated Hive adapter
```

### **Core Components**

- **Models**: `Category`, `TransactionItem`, `CategoryHive`, `TransactionItemHive`
- **State Management**: `AppState` (ChangeNotifier)
- **UI Screens**: 
  - Dashboard (transaction list with search/filter)
  - Analytics (charts and visualizations)
  - Categories (category management)
  - Add Transaction (manual entry + OCR)
- **Hive Boxes**: `transactions`, `categories`, `goals`

---

## 🚀 Getting Started

### **Prerequisites**

Before you begin, ensure you have the following installed:
- Flutter SDK (3.0 or higher)
- Dart SDK (3.0 or higher)
- Android Studio / Xcode (for mobile development)
- Git

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rupeetrack.git
   cd rupeetrack
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Generate Hive adapters** (if needed)
   ```bash
   flutter packages pub run build_runner build
   ```

4. **Run the app**
   ```bash
   flutter run
   ```

### **Backend Setup**

If you want to enable server synchronization:

1. Update the backend URL in `main.dart`:
   ```dart
   var url = 'http://YOUR_SERVER_IP:5000/add_transaction';
   ```

2. Ensure your Flask backend is running and accepts the following fields:
   - `id`, `title`, `amount`, `date`, `categoryId`
   - `storeName`, `billNo`, `items` (optional)
   - `bill_image` (multipart file)

---

## How to Use

### **Adding a Transaction**

1. Tap the **"+"** button on the Dashboard or navigate to the "Add" tab
2. Enter transaction details:
   - Title
   - Category (or create a new one)
   - Amount
   - Date
3. **Optional**: Tap the camera icon to scan a bill
4. Review extracted information and confirm
5. Tap "Add transaction"

### **Scanning a Bill**

1. While adding a transaction, tap the **camera icon** next to the amount field
2. Choose between Camera or Gallery
3. The app will automatically extract:
   - Store name
   - Bill number
   - Total amount
   - Date
   - Itemized list (if available)
4. Review and confirm the extracted data

### **Filtering Transactions**

1. On the Dashboard, tap the **"Filter"** button
2. Select filter criteria:
   - Category
   - Date range or specific date
   - Amount range (min/max)
3. Tap "Apply" to see filtered results
4. Use "Clear All" to reset filters

### **Setting Monthly Goals**

1. Navigate to the **Analytics** tab
2. Scroll to the "Monthly Goals" section
3. Tap the **"+"** or **edit icon** next to a category
4. Enter your monthly spending goal
5. The app will track your progress and alert you if you exceed the limit

### **Syncing Data**

1. Tap the **"Sync Pending"** button on the Dashboard
2. All unsynced transactions will be uploaded to the server
3. Successfully synced transactions are marked accordingly

---

## Features in Detail

### **Dashboard**
- Recent transactions list (last 10)
- Real-time search bar
- Advanced filter options
- Sync pending transactions button
- Swipe-to-delete functionality
- Tap to view full transaction details with bill image

### **Analytics**
- **Pie Chart**: Visual breakdown of spending by category
- **Bar Chart**: Category-wise spending comparison
- **Monthly Goals**: Track spending against set budgets
- Color-coded visualizations for easy understanding

### **Categories**
- Expandable list showing all categories
- Transaction count per category
- Delete categories with confirmation dialog
- Choose to uncategorize or delete associated transactions
- Dismiss individual transactions with swipe gesture

### **Add Transaction**
- Clean, intuitive form interface
- On-the-fly category creation
- OCR-powered bill scanning
- Date picker for custom dates
- Real-time form validation

---

## Data Models

### **TransactionItem**
```dart
{
  id: String,
  title: String,
  categoryId: String?,
  amount: double,
  date: DateTime,
  imgPath: String?,
  synced: bool,
  storeName: String?,
  billNo: String?,
  items: List<Map<String, dynamic>>?
}
```

### **Category**
```dart
{
  id: String,
  title: String
}
```

---

## OCR Text Extraction

The app uses advanced regex patterns to extract bill information:

- **Total Amount**: Matches "total" followed by numbers
- **Date**: Matches date formats (DD/MM/YYYY or DD-MM-YYYY)
- **Bill Number**: Matches "bill" followed by digits
- **Store Name**: Matches lines containing "store" or "company"
- **Itemized List**: Extracts table data with headers (Item, Qty, Rate, Amount)

---

## Backend API

### **Endpoint**: `POST /add_transaction`

**Request (multipart/form-data)**:
```
id: string
title: string
amount: string
date: string (ISO 8601)
categoryId: string (optional)
storeName: string (optional)
billNo: string (optional)
items: string (JSON encoded array, optional)
bill_image: file (optional)
```

**Response**: `200 OK` on success

---

## UI/UX Highlights

- Material Design 3 with deep purple color scheme
- Smooth animations and transitions
- Intuitive bottom navigation
- Floating action button for quick access
- Drawer navigation for additional screens
- Responsive layouts
- Visual feedback for all actions (SnackBars, dialogs)

---

## Dependencies

```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.0
  intl: ^0.18.0
  fl_chart: ^0.65.0
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  image_picker: ^1.0.4
  google_mlkit_text_recognition: ^0.11.0
  http: ^1.1.0

dev_dependencies:
  hive_generator: ^2.0.0
  build_runner: ^2.4.0
```

---

## Future Enhancements

- [ ] Multi-currency support
- [ ] Recurring transactions
- [ ] Export data to CSV/PDF
- [ ] Cloud backup and sync
- [ ] Biometric authentication
- [ ] Dark mode
- [ ] Custom themes
- [ ] Budget recommendations using AI
- [ ] Receipt templates for better OCR accuracy
- [ ] Split transactions among multiple categories

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate comments.

---

## Author

**Your Name**
- GitHub: [@farmersinafield](https://github.com/famersinafield-cmd)
- Email: famersinafield@gmail.com

---

## Acknowledgments

- Flutter team for the amazing framework
- Google ML Kit for OCR capabilities
- Hive team for lightweight local storage
- FL Chart for beautiful visualizations
- All open-source contributors

---

## Support

If you encounter any issues or have questions:
- Open an [issue](https://github.com/famersinafield-cmd/rupeetrack/issues)
- Email: support@rupeetrack.com

---

## Show Your Support

Give a ⭐️ if this project helped you!

---

**Made with Flutter**
