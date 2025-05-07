'''use cars365;
-- Creating Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE NOT NULL,
    Address TEXT NOT NULL,
    Role ENUM('Buyer', 'Seller', 'Both') NOT NULL,
    DateOfBirth DATE,
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creating Sellers Table
CREATE TABLE Sellers (
    SellerID INT PRIMARY KEY,
    UserID INT UNIQUE,
    StoreName VARCHAR(100) NOT NULL,
    StoreLocation VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(15) NOT NULL,
    Rating FLOAT DEFAULT 0,
    DateJoined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Creating Buyers Table
CREATE TABLE Buyers (
    BuyerID INT PRIMARY KEY,
    UserID INT UNIQUE,
    MembershipStatus VARCHAR(50),
    PreferredCarModel VARCHAR(100),
    PhoneNumber VARCHAR(15) NOT NULL,
    Address TEXT NOT NULL,
    Budget DECIMAL(12,2),
    PurchaseHistory TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Creating Cars Table
CREATE TABLE Cars (
    CarID INT PRIMARY KEY AUTO_INCREMENT,
    SellerID INT,
    Model VARCHAR(100) NOT NULL,
    Make VARCHAR(100) NOT NULL,
    Year INT NOT NULL,
    CarCondition ENUM('New', 'Used') NOT NULL,
    Engine VARCHAR(50),
    Price DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE
);

-- Creating Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    OrderStatus ENUM('Pending', 'Completed', 'Cancelled') NOT NULL,
    TotalAmount DECIMAL(12,2) NOT NULL,
    PaymentStatus ENUM('Paid', 'Pending', 'Failed') NOT NULL,
    BuyerID INT,
    SellerID INT,
    CarID INT,
    FOREIGN KEY (BuyerID) REFERENCES Buyers(BuyerID) ON DELETE CASCADE,
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating Payments Table
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT UNIQUE,
    Amount DECIMAL(12,2) NOT NULL,
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'Cash'),
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PaymentStatus ENUM('Success', 'Failed', 'Pending'),
    TransactionID VARCHAR(50) UNIQUE,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Creating Reviews Table
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT,
    BuyerID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    ReviewDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Comments TEXT,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE,
    FOREIGN KEY (BuyerID) REFERENCES Buyers(BuyerID) ON DELETE CASCADE
);

-- Creating TestDrives Table
CREATE TABLE TestDrives (
    TestDriveID INT PRIMARY KEY AUTO_INCREMENT,
    BuyerID INT,
    CarID INT,
    SellerID INT,
    TestDriveDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TestDriveStatus ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    Duration INT,
    Feedback TEXT,
    FOREIGN KEY (BuyerID) REFERENCES Buyers(BuyerID) ON DELETE CASCADE,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE,
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID) ON DELETE CASCADE
);

-- Creating VehicleVerification Table
CREATE TABLE VehicleVerification (
    VerificationID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT UNIQUE,
    InspectionNotes TEXT,
    VerificationStatus ENUM('Pending', 'Verified', 'Rejected') NOT NULL,
    VerifiedBy VARCHAR(100),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating CarOwnershipHistory Table
CREATE TABLE CarOwnershipHistory (
    HistoryID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT,
    PreviousOwnerID INT,
    PurchaseDate DATE,
    SaleDate DATE,
    OwnershipDuration VARCHAR(50),
    TransferType VARCHAR(100),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE,
    FOREIGN KEY (PreviousOwnerID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Creating Warranty Table
CREATE TABLE Warranty (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT UNIQUE,
    Provider VARCHAR(100),
    WarrantyType VARCHAR(50),
    CoverageYears INT,
    ExpiryDate DATE,
    Terms TEXT,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating Insurance Table
CREATE TABLE Insurance (
    InsuranceID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT UNIQUE,
    Provider VARCHAR(100),
    PolicyNumber VARCHAR(50) UNIQUE,
    CoverageAmount DECIMAL(12,2),
    ExpiryDate DATE,
    PremiumAmount DECIMAL(12,2),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating ServiceRecords Table
CREATE TABLE ServiceRecords (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT,
    ServiceDate DATE,
    ServiceDetails TEXT,
    ServiceCost DECIMAL(12,2),
    NextServiceDate DATE,
    ServiceCenter VARCHAR(100),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating FinancingOptions Table
CREATE TABLE FinancingOptions (
    FinanceID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT,
    FinanceProvider VARCHAR(100),
    LoanAmount DECIMAL(12,2),
    InterestRate FLOAT,
    LoanTerm VARCHAR(50),
    ApprovalStatus ENUM('Approved', 'Pending', 'Rejected'),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating EMIPlans Table
CREATE TABLE EMIPlans (
    EMIID INT PRIMARY KEY AUTO_INCREMENT,
    FinanceID INT,
    CarID INT,
    EMIAmount DECIMAL(12,2),
    EMIFrequency ENUM('Monthly', 'Quarterly', 'Yearly'),
    TotalAmount DECIMAL(12,2),
    PaymentStartDate DATE,
    Transferability ENUM('Yes', 'No'),
    FOREIGN KEY (FinanceID) REFERENCES FinancingOptions(FinanceID) ON DELETE CASCADE,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE
);

-- Creating Wishlist Table
CREATE TABLE Wishlist (
    WishlistID INT PRIMARY KEY AUTO_INCREMENT,
    CarID INT,
    BuyerID INT,
    DesiredPrice DECIMAL(12,2),
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON DELETE CASCADE,
    FOREIGN KEY (BuyerID) REFERENCES Buyers(BuyerID) ON DELETE CASCADE
);

'''