'''use cars365;
INSERT INTO Users (UserID, Name, Email, PhoneNumber, Address, Role, DateOfBirth, RegistrationDate) VALUES
(1, 'Vinay Nandagopal', 'vinay@example.com', '9876543210', 'Chennai, India', 'Both', '2001-05-10', '2024-03-06'),
(2, 'John Doe', 'john@example.com', '9876543211', 'Delhi, India', 'Buyer', '1990-08-15', '2024-03-06'),
(3, 'Alice Smith', 'alice@example.com', '9876543212', 'Mumbai, India', 'Seller', '1985-12-20', '2024-03-06'),
(4, 'Emma Wilson', 'emma@example.com', '9876543213', 'Bangalore, India', 'Both', '1993-07-25', '2024-03-06'),
(5, 'David Brown', 'david@example.com', '9876543214', 'Kolkata, India', 'Buyer', '1995-03-14', '2024-03-06');

INSERT INTO Sellers (SellerID, UserID, StoreName, StoreLocation, ContactNumber, Rating, DateJoined) VALUES
(1, 1, 'Vinay Auto Hub', 'Chennai', '9876543210', 4.8, '2024-03-06'),
(2, 3, 'Alice Motors', 'Mumbai', '9876543212', 4.5, '2024-03-06'),
(3, 4, 'Emma’s Luxury Cars', 'Bangalore', '9876543213', 4.9, '2024-03-06');

INSERT INTO Buyers (BuyerID, UserID, MembershipStatus, PreferredCarModel, PhoneNumber, Address, Budget, PurchaseHistory) VALUES
(1, 2, 'Gold', 'Honda City', '9876543211', 'Delhi, India', 800000, 'Previously bought Maruti Swift'),
(2, 4, 'Silver', 'Hyundai Creta', '9876543213', 'Bangalore, India', 1200000, 'First-time buyer'),
(3, 5, 'Bronze', 'Toyota Fortuner', '9876543214', 'Kolkata, India', 2500000, 'Previously owned Ford EcoSport');

INSERT INTO Cars (CarID, SellerID, Model, Make, Year, CarCondition, Engine, Price) VALUES
(1, 1, 'Honda City', 'Honda', 2020, 'Used', 'Petrol', 750000),
(2, 1, 'Hyundai Creta', 'Hyundai', 2022, 'New', 'Diesel', 1200000),
(3, 2, 'Maruti Swift', 'Maruti', 2021, 'Used', 'Petrol', 600000),
(4, 3, 'Toyota Fortuner', 'Toyota', 2023, 'New', 'Diesel', 3000000),
(5, 3, 'Ford EcoSport', 'Ford', 2019, 'Used', 'Petrol', 700000);

INSERT INTO Orders (OrderID, OrderDate, OrderStatus, TotalAmount, PaymentStatus, BuyerID, SellerID, CarID) VALUES
(1, '2024-03-06', 'Completed', 750000, 'Paid', 1, 1, 1),
(2, '2024-03-07', 'Pending', 1200000, 'Pending', 2, 1, 2),
(4, '2024-03-09', 'Cancelled', 3000000, 'Failed', 2, 3, 4);

INSERT INTO Payments (PaymentID, OrderID, Amount, PaymentMethod, PaymentDate, PaymentStatus, TransactionID) VALUES
(1, 1, 750000, 'Credit Card', '2024-03-06', 'Success', 'TXN123456'),
(2, 2, 1200000, 'UPI', '2024-03-07', 'Pending', 'TXN123457'),
(3, 4, 3000000, 'Net Banking', '2024-03-09', 'Failed', 'TXN123458');

INSERT INTO Reviews (ReviewID, CarID, BuyerID, Rating, ReviewDate, Comments) VALUES
(1, 1, 1, 5, '2024-03-07', 'Amazing car! Very smooth ride.'),
(2, 2, 2, 4, '2024-03-08', 'Great condition, but a bit expensive.'),
(3, 3, 3, 3, '2024-03-09', 'Average performance, but fuel-efficient.'),
(4, 4, 2, 5, '2024-03-10', 'Luxury at its best! Worth every penny.'),
(5, 5, 3, 4, '2024-03-11', 'Good car, but could have better features.');

INSERT INTO TestDrives (TestDriveID, BuyerID, CarID, SellerID, TestDriveDate, TestDriveStatus, Duration, Feedback) VALUES
(1, 1, 1, 1, '2024-03-05', 'Completed', 30, 'Smooth drive, great handling.'),
(2, 2, 2, 1, '2024-03-06', 'Completed', 45, 'Comfortable interior and smooth ride.'),
(3, 3, 3, 2, '2024-03-07', 'Cancelled', NULL, 'Cancelled due to scheduling issues.'),
(4, 2, 4, 3, '2024-03-08', 'Completed', 40, 'Powerful engine and luxury feel.'),
(5, 3, 5, 3, '2024-03-09', 'Scheduled', NULL, 'Looking forward to testing this car.');

INSERT INTO VehicleVerification (VerificationID, CarID, InspectionNotes, VerificationStatus, VerifiedBy) VALUES
(1, 1, 'Engine in excellent condition, minor scratches on body.', 'Verified', 'Inspector A'),
(2, 2, 'Brand new car, no issues detected.', 'Verified', 'Inspector B'),
(3, 3, 'Tires need replacement, minor oil leakage.', 'Pending', 'Inspector C'),
(4, 4, 'Car in perfect condition, fully serviced.', 'Verified', 'Inspector D'),
(5, 5, 'Documents missing, verification pending.', 'Pending', 'Inspector E');

INSERT INTO CarOwnershipHistory (HistoryID, CarID, PreviousOwnerID, PurchaseDate, SaleDate, OwnershipDuration, TransferType) VALUES
(1, 1, 3, '2022-05-10', '2024-01-30', '1.5 years', 'Ownership Transfer'),
(2, 2, 4, '2021-08-20', '2023-12-15', '2 years', 'Trade-In'),
(3, 3, 5, '2020-10-05', '2024-02-01', '3.5 years', 'Resale'),
(4, 4, 2, '2018-07-15', '2023-11-10', '5 years', 'Leased Return'),
(5, 5, 1, '2019-09-22', '2024-01-05', '4.3 years', 'Company Fleet Transfer');

INSERT INTO Warranty (WarrantyID, CarID, Provider, WarrantyType, CoverageYears, ExpiryDate, Terms) VALUES
(1, 1, 'Honda Care', 'Comprehensive', 3, '2027-03-06', 'Covers engine, transmission, and electrical components.'),
(2, 2, 'Hyundai Shield', 'Powertrain', 5, '2029-03-07', 'Covers engine and transmission only.'),
(3, 3, 'Maruti Secure', 'Standard', 2, '2026-03-08', 'Covers basic components, excluding wear & tear.'),
(4, 4, 'Toyota Protection', 'Comprehensive', 4, '2028-03-09', 'Full coverage including accidental damage.'),
(5, 5, 'Ford Warranty Plus', 'Powertrain', 3, '2027-03-10', 'Limited to powertrain parts replacement.');

INSERT INTO Insurance (InsuranceID, CarID, Provider, PolicyNumber, CoverageAmount, ExpiryDate, PremiumAmount) VALUES
(1, 1, 'ICICI Lombard', 'POL123456', 500000, '2025-12-31', 15000),
(2, 2, 'HDFC Ergo', 'POL123457', 750000, '2026-11-30', 18000),
(3, 3, 'Bajaj Allianz', 'POL123458', 600000, '2025-10-15', 14000),
(4, 4, 'Reliance General', 'POL123459', 900000, '2027-09-25', 22000),
(5, 5, 'TATA AIG', 'POL123460', 550000, '2026-08-10', 16000);

INSERT INTO ServiceRecords (ServiceID, CarID, ServiceDate, ServiceDetails, ServiceCost, NextServiceDate, ServiceCenter) VALUES
(1, 1, '2024-01-20', 'Oil change and filter replacement', 5000, '2024-07-20', 'Honda Service Center'),
(2, 2, '2024-02-10', 'Brake pad replacement', 8000, '2024-08-10', 'Hyundai Service Hub'),
(3, 3, '2024-01-05', 'Battery replacement', 10000, '2024-07-05', 'Maruti Suzuki Workshop'),
(4, 4, '2023-12-15', 'Full car servicing and alignment', 15000, '2024-06-15', 'Toyota Authorized Service'),
(5, 5, '2024-02-25', 'Tire rotation and engine tuning', 7000, '2024-08-25', 'Ford Service Station');

INSERT INTO FinancingOptions (FinanceID, CarID, FinanceProvider, LoanAmount, InterestRate, LoanTerm, ApprovalStatus) VALUES
(1, 1, 'HDFC Bank', 500000, 8.5, '5 years', 'Approved'),
(2, 2, 'ICICI Bank', 800000, 7.2, '4 years', 'Pending'),
(3, 3, 'SBI Auto Loan', 450000, 9.0, '6 years', 'Approved'),
(4, 4, 'Axis Bank', 1200000, 6.9, '5 years', 'Rejected'),
(5, 5, 'Kotak Mahindra', 550000, 7.5, '3 years', 'Approved');

INSERT INTO EMIPlans (EMIID, FinanceID, CarID, EMIAmount, EMIFrequency, TotalAmount, PaymentStartDate, Transferability) VALUES
(1, 1, 1, 10500, 'Monthly', 630000, '2024-04-01', 'Yes'),
(2, 2, 2, 17500, 'Monthly', 840000, '2024-05-01', 'No'),
(3, 3, 3, 8500, 'Monthly', 510000, '2024-03-15', 'Yes'),
(4, 5, 5, 15000, 'Quarterly', 600000, '2024-06-01', 'No');

INSERT INTO Wishlist (WishlistID, CarID, BuyerID, DesiredPrice, DateAdded) VALUES
(1, 1, 1, 700000, '2024-03-06'),
(2, 2, 2, 1100000, '2024-03-07'),
(3, 3, 3, 550000, '2024-03-08'),
(4, 4, 2, 2900000, '2024-03-09'),
(5, 5, 3, 650000, '2024-03-10');
'''