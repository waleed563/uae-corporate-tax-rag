# Ring 3 RAG — results to grade

Config: parent=2000, child=300, cosine_k=30, rerank_k=5, variants=3, compress_prose=0.28/example=0.4, max_sents=20, token_budget=3500, pysbd=True

## Q1 — Simple lookup
**Question:** What's the corporate tax rate in the UAE?

**Query variants:**
- What is the applicable corporate tax rate in the United Arab Emirates?
- Could you specify the prevailing corporate tax rate within the jurisdiction of the UAE?
- What is the statutory corporate tax rate enforced in the United Arab Emirates?

**Tokens in context:** 1496

**Answer:** Corporate Tax in the UAE is imposed at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding a specified amount, and 9% (nine percent) on the portion of the Taxable Income exceeding that amount. The specific amounts are not provided in the context. Source: page 20 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 13 [prose] (rerank 3.6747, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…
- [rank 2] page 19 [prose] (rerank 2.7804, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Corporate Tax Law Implementing Decisions on the Ministry of Finance and FTA websites Corporate Tax FTA Decisions on the FTA website General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter…
- [rank 3] page 21 [example] (rerank 2.3527, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax A LLC is a company incorporated in the UAE. • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: • The portion of the Taxable income exceeding AED 375,000 will be subject to Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% =…
- [rank 4] page 38 [example] (rerank 1.6083, compressed 248→20 sentences) During the Tax Period it has a total Revenue of AED 80,000,000. Tax under the general rates, and complies with the transfer pricing rules and other documentation requirements set out in the Corporate Tax Law. 70 Article 4(1) of the Corporate Tax Law. Activity and will be required to register for Cor…
- [rank 5] page 20 [prose] (rerank 1.1547, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…

## Q2 — Simple lookup
**Question:** When did corporate tax actually start in the UAE?

**Query variants:**
- What is the effective commencement date of corporate taxation in the United Arab Emirates?
- At what point in time did the implementation of corporate tax legislation begin in the UAE?
- Can you specify the initiation date of corporate tax obligations within the jurisdiction of the United Arab Emirates?

**Tokens in context:** 1410

**Answer:** The provisions of the Corporate Tax Law shall apply to Tax Periods commencing on or after 1 June 2023. Source: page 13 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 13 [prose] (rerank 3.0069, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…
- [rank 2] page 21 [example] (rerank 0.73, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax A LLC is a company incorporated in the UAE. For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period. • The first AED 375,000 of Taxable Income will be subject to Corpor…
- [rank 3] page 53 [example] (rerank -0.5437, compressed 24→6 sentences) During the Financial Year ending 31 December 2025, S LLC, a UAE resident company, recognised a revaluation loss in its Financial Statements in respect of an asset measured at fair value. Several exemptions are provided for within the Corporate Tax regime.135 135 Articles 22 to 25 of the Corporate Ta…
- [rank 4] page 14 [prose] (rerank -1.1684, compressed 20→8 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Subsequent chapters are organised by subject matter to cover the fundamentals of the Corporate Tax regime in the UAE. This includes what Corporate Tax is, who is subject to Corporate Tax, what types of income are taxable, and how a Taxable Person…
- [rank 5] page 18 [prose] (rerank -1.4198, compressed 25→13 sentences) Corporations and Businesses is referred to as “FTA Decision No. 5 of 2023”; Federal Tax Authority Decision No. 6 of 2023 on Tax Deregistration Timeline for the Purposes of Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses is referred to as “FTA Decision No. 6 of 2023”;…

## Q3 — Simple lookup
**Question:** How much profit can I make before I owe any corporate tax?

**Query variants:**
- What is the threshold of taxable income that must be exceeded before corporate tax liabilities are incurred?
- What is the maximum allowable profit exempt from corporate taxation prior to the imposition of tax obligations?
- What is the limit of profit generation that triggers the liability for corporate tax assessment?

**Tokens in context:** 1291

**Answer:** You can make a profit up to a certain amount before owing any corporate tax, as the first portion of your taxable income is subject to a 0% corporate tax rate. Specifically, the first AED 375,000 of taxable income will be taxed at 0%. Therefore, you can make a profit of up to AED 375,000 without incurring any corporate tax liability. 

Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank -0.838, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax A LLC’s Taxable Income for its Tax Period will be the accounting net profit (or loss) of the business, after making tax adjustments for certain items specified in the Corporate A LLC’s Corporate Tax liability will be calculated as follows: • The first AED 375,…
- [rank 2] page 20 [prose] (rerank -4.267, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…
- [rank 3] page 68 [example] (rerank -4.713, compressed 41→7 sentences) Profit Before Tax of AED 60,000,000 for its Financial Year ending 31 December 2025. 183 Article 31(1)(a) of the Corporate Tax Law. General Corporate Tax Guide | Corporate Tax | CTGGCT1 The purpose of this provision is to prevent the Corporate Tax base from being eroded by transactions and arrangemen…
- [rank 4] page 111 [example] (rerank -5.8637, compressed 84→20 sentences) Example 35: Application of Corporate Tax rates to Tax Groups Corporate Tax liability calculation would be as follows: Corporate Tax Payable (AED) Total Corporate Tax due per company Total Corporate Tax Payable for all three companies If these companies formed a Tax Group, the Corporate Tax due on th…
- [rank 5] page 19 [prose] (rerank -6.0957, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter sets out a brief overview of the core principles of Corporate Tax and how the Corporate Tax system functions as a whole. What is Co…

## Q4 — Simple lookup
**Question:** After my financial year ends, how long do I have to file my return?

**Query variants:**
- What is the statutory deadline for the submission of my tax return following the conclusion of my financial year?
- What is the prescribed timeframe for filing my tax return subsequent to the termination of my financial year?
- What is the regulatory period allowed for the filing of my return after the end of my fiscal year?

**Tokens in context:** 256

**Answer:** This is not covered in the provided document.  
Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 87 [example] (rerank -7.4266, compressed 39→3 sentences) When filing its first Tax Return for the Tax Period ended 31 May 2024, G LLC made an election to adjust its Taxable Income for the purposes of calculating gains or losses on the Dubai property using the time apportionment method. Tax Period where the conditions are satisfied. 2026), can elect to be …
- [rank 2] page 89 [example] (rerank -8.3674, compressed 16→4 sentences) His Tax Period ends on 31 December each year. Period in any Tax Period. In the most recent Tax Period ending 31 December 2025, Mr Tax Return.
- [rank 3] page 93 [example] (rerank -8.8173, compressed 73→3 sentences) 1,200,000 – AED 800,000) in the Tax Return for the Tax Period in which D LLC subsequently transferred the asset. The Financial Year of each of the Taxable Persons ends on the same date;278 The Taxable Persons prepare their Financial Statements using the same accounting standards;279 and
- [rank 4] page 3 [prose] (rerank -9.0288, compressed 16→3 sentences) Tax Period Income exempt under the participation exemption General deductibility rules
- [rank 5] page 2 [prose] (rerank -10.2653, compressed 18→3 sentences) Registration and record keeping obligations of Exempt Persons Taxable Income Tax Period

## Q5 — Conditional
**Question:** My free-zone company made AED 2 million profit — do I pay 0%?

**Query variants:**
- Is my free-zone entity, having generated a profit of AED 2 million, subject to a corporate tax rate of 0%?
- Does the profit of AED 2 million earned by my free-zone company exempt it from corporate taxation at the rate of 0%?
- In light of my free-zone company's profit of AED 2 million, am I liable for corporate tax at a rate of 0%?

**Tokens in context:** 2075

**Answer:** To determine if your free-zone company pays 0% Corporate Tax on the AED 2 million profit, you need to assess whether the income qualifies as Qualifying Income. If the income is Qualifying Income, the first AED 375,000 of Taxable Income will be subject to 0% Corporate Tax. However, if the income does not qualify, the standard Corporate Tax rate may apply to the portion exceeding AED 375,000. 

Additionally, ensure that your company meets the requirements to be considered a Qualifying Free Zone Person. If it does, you may benefit from the 0% rate on the first AED 375,000 of Taxable Income. 

Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank 1.8002, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax A LLC is a company incorporated in the UAE. LLC generated Revenue of AED 8 million and incurred expenses of AED 2 million, resulting in a net profit of AED 6 million per its Financial Statements. A LLC’s Taxable Income for its Tax Period will be the accounting…
- [rank 2] page 111 [example] (rerank -1.1282, compressed 84→20 sentences) If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Corporate Tax Payable (AED) Total Corporate Tax due per company Total Corporate Tax Payable for all three companies Income of AED 15,0…
- [rank 3] page 38 [example] (rerank -1.2612, compressed 248→20 sentences) During the Tax Period it has a total Revenue of AED 80,000,000. H LLC maintains adequate substance in the Free Zone, has not made an election to be subject to UAE Corporate Tax under the general rates, and complies with the transfer pricing rules and other documentation requirements set out in the C…
- [rank 4] page 38 [example] (rerank -3.2707, compressed 7→5 sentences) F LLC and G LLC are both Free Zone Persons. F LLC (a Qualifying Free Zone Person) owns a number of warehouses located in a Free Zone. As the transaction is between two Free Zone Persons, and the sale relates to Commercial Property in a Free Zone, the income earned on the sale is Qualifying Income an…
- [rank 5] page 68 [example] (rerank -4.7678, compressed 41→19 sentences) C LLC has Revenue of AED 150,000,000, adjusted EBITDA of AED 130,000,000 and Profit Before Tax of AED 60,000,000 for its Financial Year ending 31 December 2025. In 2025, C LLC incurs costs including Interest expenditure of AED 80,000,000. C LLC also receives Interest income of AED 30,000,000, result…

## Q6 — Conditional
**Question:** My business is tiny with very low revenue. Is there relief so I pay nothing?

**Query variants:**
- Is there a provision for tax relief applicable to micro-enterprises with minimal revenue, allowing for a zero tax liability?
- Are there any exemptions or relief measures available for small businesses with negligible income that would result in no corporate tax obligation?
- What mechanisms exist within the corporate tax framework to provide relief for businesses with limited revenue, potentially resulting in a zero tax payment?

**Tokens in context:** 480

**Answer:** If your business's Revenue does not exceed the small business relief threshold of AED 3,000,000 per Tax Period, you may be eligible for small business relief. However, to benefit from this relief, you must make an election in your Tax Period. If you elect for small business relief, you will not be liable for Corporate Tax as long as your Revenue remains below the threshold. 

It's important to note that if your Revenue exceeds the threshold in any Tax Period, you will not be eligible for small business relief for that period. 

Source: page 89 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 89 [example] (rerank -1.2844, compressed 16→4 sentences) Example 27: Electing for small business relief To date, Mr X’s Revenue has never exceeded the small business relief threshold of AED 3,000,000 per Tax Mr X is eligible to benefit from small business relief as his Revenue for the 31 December In order to benefit from the relief, he must make an electi…
- [rank 2] page 89 [example] (rerank -4.2752, compressed 66→7 sentences) Example 28: Carried forward unutilised Tax Losses when electing for small business relief In the prior year, C LLC’s Revenue did not exceed the AED 3,000,000 relief threshold. C LLC elects for small business relief for the Tax Period ending 31 December 2025. LLC’s carried forward Tax Losses cannot b…
- [rank 3] page 4 [prose] (rerank -6.5784, compressed 18→12 sentences) Business restructuring relief Taxation of partnership and their partners Unincorporated Partnerships Tax treatment of a foreign partnership Tax Group regime Requirements to form a Tax Group Compliance with Corporate Tax requirements Taxable Income of a Tax Group 9. How is any Corporate Tax liability…
- [rank 4] page 96 [example] (rerank -8.2076, compressed 98→3 sentences) Business restructuring relief shall no longer apply because there is a subsequent transfer of the Business which was transferred. For further details on business restructuring relief, readers are advised to consult Ministerial Decision No. 133 of 2023 on Business Restructuring Relief.292
- [rank 5] page 3 [prose] (rerank -9.3231, compressed 15→8 sentences) Tax Losses Tax Loss relief Tax Losses and change of ownership Transfer of Tax Losses Determination of Taxable Income 7. Reliefs Small business relief Business restructuring relief

## Q7 — Conditional
**Question:** My profit is below the threshold — do I still have to register at all?

**Query variants:**
- Is it necessary for an entity with profits below the established threshold to complete the registration process?
- Does an organization with earnings that fall below the specified threshold still have an obligation to register?
- Is registration required for a taxpayer whose net profit does not exceed the designated threshold?

**Tokens in context:** 428

**Answer:** If your profit is below the threshold, you may still be required to register for Corporate Tax purposes if you are engaged in activities that are not considered Excluded Activities. Additionally, if you are an Exempt Person, you must notify the Ministry and meet relevant conditions to be exempt from registration. Therefore, whether you need to register depends on the nature of your activities and your status as an Exempt Person. 

Source: page 2 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 2 [prose] (rerank -10.1228, compressed 18→14 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Excluded Activities Qualifying Activities The de minimis requirement Election to be taxed at the general rates of Corporate Tax Exempt Persons Types of Exempt Persons Automatically Exempt Persons Exempt Persons if they notify the Ministry, and me…
- [rank 2] page 38 [example] (rerank -10.2675, compressed 248→4 sentences) Exempt if they notify the Ministry of Finance, and meet relevant conditions: Activity and will be required to register for Corporate Tax.75 Revenue, it will be required to register with the FTA for Corporate Tax.77 Registration and record keeping obligations of Exempt Persons
- [rank 3] page 21 [example] (rerank -10.8993, compressed 112→3 sentences) This includes the obligation to register for Corporate Tax purposes, file a Tax Return and retain all relevant documents and records to support their Corporate Tax filings. Taxable Persons must calculate their Taxable Income on an annual basis using their accounting net profit or loss for the releva…
- [rank 4] page 37 [example] (rerank -11.0315, compressed 9→3 sentences) E LLC is a Free Zone Person, and generates all of its income from leasing a property which is not located in a Free Zone. As this is Revenue from an Excluded Activity, this income is not Qualifying Income. As E LLC only earns non-qualifying Revenue, it will not satisfy the de minimis requirement and…
- [rank 5] page 58 [example] (rerank -11.057, compressed 66→3 sentences) Participation exemption for other income and gains Other income and gains may also be exempt if they are derived from a Participating The requirements for a Participating Interest in both a Resident and Non-Resident are the same, save that in relation to a Participation Interest in a Resident, a Par…

## Q8 — Conditional
**Question:** I personally earn rent from a flat I own. Is that taxed?

**Query variants:**
- Does the income derived from rental property ownership by an individual constitute taxable income under the UAE Corporate Tax framework?
- Is the rental income generated from personal real estate holdings subject to taxation in accordance with UAE Corporate Tax regulations?
- Is the revenue obtained from leasing a residential property owned by an individual liable for taxation under the provisions of the UAE Corporate Tax law?

**Tokens in context:** 361

**Answer:** The context specifies that personal investment activities conducted by a natural person for their personal account, which are neither conducted through a License nor considered a commercial business, are not subject to Corporate Tax. Therefore, if your rental income is derived from personal investment and does not meet the criteria of being a commercial business, it would not be taxed under the Corporate Tax Law. 

Source: page 10 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 2 [prose] (rerank -8.0117, compressed 18→5 sentences) Election to be taxed at the general rates of Corporate Tax Registration and record keeping obligations of Exempt Persons 6. What is subject to Corporate Tax? Taxable Income Tax Period
- [rank 2] page 56 [example] (rerank -8.4099, compressed 47→3 sentences) The income was mainly derived from operating the hotels it owns. As dividends received from UAE Resident Persons are exempt from Corporate Tax, this amount should be excluded when calculating Taxable Income. The Participation is subject to Corporate Tax, or a similar tax, in the country in which it …
- [rank 3] page 38 [example] (rerank -8.7533, compressed 7→3 sentences) Example 4: Qualifying Income As the transaction is between two Free Zone Persons, and the sale relates to Commercial Property in a Free Zone, the income earned on the sale is Qualifying Income and is eligible for the
- [rank 4] page 10 [prose] (rerank -9.8472, compressed 16→4 sentences) Personal Investment: Investment activity that a natural person conducts for their personal account that is neither conducted through a Licence or requiring a Licence from a Licensing Authority in the UAE, nor considered as a commercial business in accordance with the Federal Decree-Law No. 50 of 202…
- [rank 5] page 114 [example] (rerank -9.9953, compressed 242→3 sentences) Taxable Person. Taxable Persons that earn Revenue that does not exceed AED 3,000,000 in the Tax Where a Taxable

## Q9 — Multi-hop
**Question:** As a free-zone company, what exactly counts as 'qualifying income' for the 0%?

**Query variants:**
- What constitutes 'qualifying income' eligible for the 0% tax rate for entities operating within a free-zone jurisdiction?
- In the context of a free-zone entity, which categories of income are classified as 'qualifying income' for the purpose of the 0% corporate tax rate?
- Could you delineate the specific types of income that are recognized as 'qualifying income' for the application of the 0% tax rate for companies established in a free-zone?

**Tokens in context:** 1017

**Answer:** Qualifying Income for a Free Zone company is any income derived by a Qualifying Free Zone Person that meets the conditions specified in Article 18 of the Corporate Tax Law. Specifically, it includes income from transactions between Free Zone Persons related to Commercial Property located in a Free Zone, provided that the other relevant requirements are met. However, income from activities that are classified as Excluded Activities, such as leasing property not located in a Free Zone, does not qualify. Therefore, to be eligible for the 0% Corporate Tax rate, the income must be derived from qualifying activities as defined by the law. 

Source: page 38 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 38 [example] (rerank 5.0474, compressed 7→6 sentences) Example 4: Qualifying Income F LLC and G LLC are both Free Zone Persons. F LLC (a Qualifying Free Zone Person) owns a number of warehouses located in a Free Zone. As the transaction is between two Free Zone Persons, and the sale relates to Commercial Property in a Free Zone, the income earned on the…
- [rank 2] page 37 [example] (rerank 0.7938, compressed 9→4 sentences) E LLC is a Free Zone Person, and generates all of its income from leasing a property which is not located in a Free Zone. As this is Revenue from an Excluded Activity, this income is not Qualifying Income. As E LLC only earns non-qualifying Revenue, it will not satisfy the de minimis requirement and…
- [rank 3] page 10 [prose] (rerank -2.2368, compressed 16→13 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Personal Investment: Investment activity that a natural person conducts for their personal account that is neither conducted through a Licence or requiring a Licence from a Licensing Authority in the UAE, nor considered as a commercial business i…
- [rank 4] page 4 [prose] (rerank -2.8045, compressed 18→10 sentences) Corporate Tax rates for Qualifying Free Zone Persons Withholding Tax rate Tax credits General Corporate Tax Guide | Corporate Tax | CTGGCT1 Requirements for the Withholding Tax Credit Foreign Tax Credit Impact of Double Taxation Agreements on Foreign Tax credits Administration of Corporate Tax Tax R…
- [rank 5] page 111 [example] (rerank -3.1396, compressed 84→20 sentences) Taxable Income (AED) Taxable Income (AED) Corporate Tax rates for Qualifying Free Zone Persons Corporate Tax applies to Qualifying Free Zone Persons at the following rates:347 Qualifying Income Taxable Income that is not Qualifying Income The Corporate Tax rate applied to Qualifying Free Zone Person…

## Q10 — Multi-hop
**Question:** Can my group of companies be taxed as one, and what must we meet?

**Query variants:**
- Is it permissible for my corporate group to be treated as a single taxable entity, and what criteria must be satisfied to achieve this status?
- Can my consortium of enterprises be consolidated for taxation purposes, and what requirements must be fulfilled to qualify for such treatment?
- Is it allowable for my affiliated companies to be assessed as a unified taxable group, and what conditions must be met to obtain this designation?

**Tokens in context:** 1153

**Answer:** Yes, your group of companies can be taxed as one by forming a Tax Group. To do this, the companies must meet specific ownership requirements and apply to the Federal Tax Authority (FTA) for approval. Additionally, the parent company must be able to consolidate the accounting income of each company in the group and make necessary tax adjustments, including applying any tax losses at the group level. If the ownership conditions are no longer met, the companies may cease to be part of the Tax Group. 

Source: page 107 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 111 [example] (rerank -3.5147, compressed 84→20 sentences) Example 35: Application of Corporate Tax rates to Tax Groups If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Each company’s Corporate Tax liability calculation would be as follows: Total Corporate Tax du…
- [rank 2] page 92 [example] (rerank -3.9701, compressed 21→4 sentences) C LLC and D LLC also meet all other conditions to be considered as members of a Qualifying Taxable Income, C LLC will be treated as having received AED 800,000 and D LLC will be treated as having paid AED 800,000 for the machinery. 271 Article 26(5) of the Corporate Tax Law. General Corporate Tax Gu…
- [rank 3] page 107 [example] (rerank -6.6663, compressed 87→20 sentences) Example 34: Formation of a Tax Group C LLC, therefore, meets the ownership requirements of F LLC and Z LLC in order to form a Tax C LLC (as the Parent Company), F LLC and Z LLC made an application to form a Tax The application to form a Tax Group was approved by the FTA. Group’s first Tax Period on …
- [rank 4] page 48 [example] (rerank -7.8031, compressed 121→20 sentences) Financial Statements and calculate the Taxable Income of the Business as if it were a separate and independent Business. General Corporate Tax Guide | Corporate Tax | CTGGCT1 6. What is subject to Corporate Tax? For Corporate Tax purposes, the tax base is a Taxable Person’s Taxable Income. General C…
- [rank 5] page 4 [prose] (rerank -7.8323, compressed 18→15 sentences) Business restructuring relief Taxation of partnership and their partners Unincorporated Partnerships Incorporated partnerships Tax treatment of a foreign partnership Tax Group regime Requirements to form a Tax Group Formation and cessation of a Tax Group Joining or leaving a Tax Group Compliance wit…

## Q11 — Multi-hop
**Question:** My business made a loss last year — can I use it to cut this year's tax?

**Query variants:**
- Is it permissible to offset the prior fiscal year's losses against the taxable income for the current financial year?
- Can the losses incurred in the preceding tax year be utilized to reduce the taxable liability for the current assessment period?
- Am I entitled to apply the losses from the prior year to mitigate the tax obligations for the present year?

**Tokens in context:** 1487

**Answer:** You can use your business's tax loss from the previous year to offset this year's taxable income, but there are specific conditions. If your business has a tax loss carried forward, you can utilize it against your taxable income in the current tax period, subject to a maximum utilization limit of 75% of your taxable income for that period. Additionally, if there has been a change in ownership of more than 50%, the tax losses can still be carried forward, provided that the same or similar business is continued after the change in ownership. 

If you have elected for small business relief in the current tax period, you will not be able to use the carried forward tax losses in that period, but you can carry them forward to future periods when the small business relief is not elected, provided the relevant conditions are met. 

Source: page 80, 89 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 80 [example] (rerank -4.0839, compressed 84→20 sentences) Example 22: Carried forward Tax Losses In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. • In the Tax Period ending on 31 December 2026, C LLC makes a Tax Loss and there are no amounts to be taxed. This means that the maximum Tax Loss that can be used to offset against …
- [rank 2] page 89 [example] (rerank -4.9063, compressed 66→12 sentences) Example 28: Carried forward unutilised Tax Losses when electing for small business relief At the beginning of the Tax Period, C LLC had unutilised Tax Losses of AED 400,000. C LLC elects for small business relief for the Tax Period ending 31 December 2025. LLC’s carried forward Tax Losses cannot be …
- [rank 3] page 21 [example] (rerank -7.8991, compressed 112→7 sentences) A LLC’s Taxable Income for its Tax Period will be the accounting net profit (or loss) of the business, after making tax adjustments for certain items specified in the Corporate For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 mi…
- [rank 4] page 83 [example] (rerank -8.8019, compressed 28→11 sentences) Example 23: Transfer of Tax Losses C LLC makes a loss of AED 2,000,000 and F LLC makes a profit of AED 2,000,000 in the same Tax Period. C LLC chooses to transfer AED 1,500,000 of Tax Losses to F This is the maximum amount that F LLC can offset against its Taxable Income. The remaining AED 500,000 o…
- [rank 5] page 87 [example] (rerank -8.8316, compressed 39→9 sentences) When filing its first Tax Return for the Tax Period ended 31 May 2024, G LLC made an election to adjust its Taxable Income for the purposes of calculating gains or losses on the Dubai property using the time apportionment method. Given that the Immovable Property was owned for two years in total and…

## Q12 — Multi-hop
**Question:** What records must I keep, and for how long, to stay compliant?

**Query variants:**
- What documentation is required to be maintained, and for what duration, to ensure compliance with regulatory obligations?
- What records are mandated for retention, and what is the prescribed retention period to adhere to compliance standards?
- Which specific records are necessary to retain, and what is the requisite timeframe for retention to fulfill compliance requirements?

**Tokens in context:** 242

**Answer:** You must maintain records that evidence your exempt status if you are an Exempt Person. These records should be kept for 7 years from the end of the relevant tax period. Additionally, if your business becomes subject to Corporate Tax, you may need to maintain Financial Statements, although there are administrative simplifications to support compliance. 

Source: page 38 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 4 [prose] (rerank -9.2858, compressed 18→3 sentences) Requirements to form a Tax Group Compliance with Corporate Tax requirements 9. How is any Corporate Tax liability calculated?
- [rank 2] page 2 [prose] (rerank -9.522, compressed 18→7 sentences) Qualifying Activities Adequate substance requirements Types of Exempt Persons Automatically Exempt Persons Exempt Persons if they notify the Ministry, and meet relevant conditions Registration and record keeping obligations of Exempt Persons Tax Period
- [rank 3] page 4 [prose] (rerank -10.0558, compressed 18→5 sentences) Requirements for the Withholding Tax Credit Registration and Deregistration Tax Returns and payments Record keeping How long should records be kept?
- [rank 4] page 38 [example] (rerank -10.8482, compressed 248→3 sentences) For the purposes of monitoring compliance with the exemption requirements, the FTA may request any relevant information or records from a Qualifying Public Benefit Entity Registration and record keeping obligations of Exempt Persons However, Exempt Persons are required to maintain records which evid…
- [rank 5] page 48 [example] (rerank -10.9148, compressed 121→3 sentences) The Authority must maintain 49 adjustments made, generally, there is no need to maintain two sets of records. For some businesses, becoming subject to Corporate Tax may involve new requirements to maintain Financial Statements, although there are certain administrative simplifications to support the…

## Q13 — Describe-your-business
**Question:** I freelance from home in Dubai with no trade licence — do I owe corporate tax?

**Query variants:**
- Does the absence of a trade license for my freelance activities conducted from my residence in Dubai render me liable for corporate tax obligations?
- Am I subject to corporate tax liabilities given my status as a home-based freelancer in Dubai operating without a trade license?
- In the context of my freelance operations in Dubai, which are conducted from my domicile and lack a formal trade license, am I required to fulfill corporate tax obligations?

**Tokens in context:** 2345

**Answer:** As a freelancer operating from home in Dubai without a trade licence, you are not conducting a business that is required to be licensed. Therefore, you would not be subject to Corporate Tax on your income, as Corporate Tax does not apply to individuals' salaries, wages, and other employment income. However, if your activities are considered a business or business activity, you may need to register for Corporate Tax. Since you mentioned not having a trade licence, it suggests that you may not be conducting a licensed business, which means you likely do not owe Corporate Tax. 

Source: page 26 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 26 [example] (rerank -4.8051, compressed 298→20 sentences) Residence for Corporate Tax purposes is not determined by where a natural person resides or is domiciled. For natural persons, residence for Corporate Tax purposes is concerned with the person’s business connection to the UAE. It is this connection, rather than other factors such as nationality or w…
- [rank 2] page 7 [prose] (rerank -5.6928, compressed 15→11 sentences) and conducted by a Qualifying Free Zone Person from which non-Qualifying Income is derived. Exempt Person: A Person exempt from Corporate Tax under Article 4 of the Corporate Tax Law. Extractive Business: The Business or Business Activity of exploring, extracting, removing, or otherwise producing an…
- [rank 3] page 114 [example] (rerank -5.7965, compressed 242→20 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that woul…
- [rank 4] page 38 [example] (rerank -6.4352, compressed 248→20 sentences) H LLC maintains adequate substance in the Free Zone, has not made an election to be subject to UAE Corporate During the Tax Period, it undertakes a small number of transactions with individuals and earns AED 4,500,000 of Revenue. Whilst some of these structures and arrangements are by default treate…
- [rank 5] page 48 [example] (rerank -7.167, compressed 121→20 sentences) As the Authority is conducting a Business under a Licence, the Authority will be treated as a Taxable Person in relation to this Business only. Financial Statements and calculate the Taxable Income of the Business as if it were a separate and independent Business. This does not impact the exempt sta…

## Q14 — Describe-your-business
**Question:** I run a free-zone online store selling to mainland UAE customers — how am I taxed?

**Query variants:**
- What are the tax implications for a free-zone e-commerce entity engaging in sales to customers located in mainland UAE?
- How is a free-zone online retail business subject to taxation when transacting with consumers in the mainland UAE jurisdiction?
- What is the applicable corporate tax framework for a free-zone online store conducting sales to mainland UAE clientele?

**Tokens in context:** 1269

**Answer:** If you run a free-zone online store selling to mainland UAE customers, your tax situation will depend on the nature of your activities. Generally, if your revenue from sales to individuals in the mainland exceeds the de minimis threshold, which is specified as the lower of a certain amount, you may not be eligible for the exemption from Corporate Tax. Additionally, if your activities are classified as Excluded Activities, you may also be subject to Corporate Tax. Therefore, it is essential to assess your total revenue from mainland customers and the nature of your transactions to determine your tax obligations. 

Source: page 38 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 38 [example] (rerank -0.3819, compressed 248→20 sentences) H LLC is a Free Zone Person that sells vehicles to other Free Zone Persons. During the Tax Period it has a total Revenue of AED 80,000,000. H LLC maintains adequate substance in the Free Zone, has not made an election to be subject to UAE Corporate Tax under the general rates, and complies with the …
- [rank 2] page 38 [example] (rerank -2.3037, compressed 7→4 sentences) F LLC and G LLC are both Free Zone Persons. F LLC (a Qualifying Free Zone Person) owns a number of warehouses located in a Free Zone. As the transaction is between two Free Zone Persons, and the sale relates to Commercial Property in a Free Zone, the income earned on the sale is Qualifying Income an…
- [rank 3] page 8 [prose] (rerank -2.9316, compressed 17→7 sentences) conditions of Article 47(2) of the Corporate Tax Law. Free Zone: A designated and defined geographic area within the UAE that is specified in a decision issued by the Cabinet at the suggestion of the Minister. Free Zone Person: A juridical person incorporated, established, or otherwise registered in…
- [rank 4] page 10 [prose] (rerank -4.7947, compressed 21→9 sentences) renewable, non-living natural resources that may be extracted from the UAE’s Corporate Tax Law. Non-Extractive Natural Resource Business: The Business or Business Activity of separating, treating, refining, processing, storing, transporting, marketing or distributing the Natural Resources of the UAE…
- [rank 5] page 7 [prose] (rerank -4.8612, compressed 15→9 sentences) and conducted by a Qualifying Free Zone Person from which non-Qualifying Income is derived. Exempt Person: A Person exempt from Corporate Tax under Article 4 of the Corporate Tax Law. Extractive Business: The Business or Business Activity of exploring, extracting, removing, or otherwise producing an…

## Q15 — Describe-your-business
**Question:** We're a 3-person startup with no profit yet. Any corporate tax obligations?

**Query variants:**
- Does our three-member startup, which has yet to generate any profit, incur any corporate tax liabilities?
- Are there any corporate tax obligations applicable to our startup, comprised of three individuals, in the absence of profit generation?
- What corporate tax responsibilities, if any, are imposed on our three-person startup that has not yet realized any profits?

**Tokens in context:** 723

**Answer:** As a startup with no profit, you may not have a Corporate Tax liability since Corporate Tax is imposed on Taxable Income. However, you still have obligations to register for Corporate Tax purposes, file a Tax Return, and retain all relevant documents and records to support your Corporate Tax filings. If you meet the relevant requirements, you may also benefit from small business relief. 

Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank -7.5642, compressed 112→13 sentences) Example 1: Calculation of Corporate Tax A LLC’s Corporate Tax liability will be calculated as follows: • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: In order to calculate its UAE Corporate Tax payable, A LLC will need to consider if there are any available tax cre…
- [rank 2] page 1 [prose] (rerank -7.6581, compressed 19→7 sentences) Corporate Tax – General Corporate Tax Guide | CTGGCT1 General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? What is Corporate Tax? How does Corporate Tax work? 5. Who is subject to Corporate Tax?
- [rank 3] page 48 [example] (rerank -8.1032, compressed 121→3 sentences) 6. What is subject to Corporate Tax? For some businesses, becoming subject to Corporate Tax may involve new requirements to maintain Financial Statements, although there are certain administrative simplifications to support these businesses and manage such burdens. 129 Article 20(3) of the Corporate…
- [rank 4] page 19 [prose] (rerank -8.3918, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter sets out a brief overview of the core principles of Corporate Tax and how the Corporate Tax system functions as a whole. What is Co…
- [rank 5] page 58 [example] (rerank -8.7108, compressed 66→3 sentences) Corporate Tax on: 149 Article 23(4) of the Corporate Tax Law. (c) of the Corporate Tax Law.

## Q16 — Describe-your-business
**Question:** My mainland trading company made AED 500,000 profit — roughly what do I owe?

**Query variants:**
- What is the estimated tax liability for my mainland trading entity that has generated a profit of AED 500,000?
- Can you provide an approximation of the corporate tax obligation for my mainland trading company with a profit of AED 500,000?
- What would be the anticipated corporate tax due for my mainland trading firm reporting a profit of AED 500,000?

**Tokens in context:** 1593

**Answer:** To determine the Corporate Tax liability for your mainland trading company with a profit of AED 500,000, you need to consider the following conditions:

1. The first AED 375,000 of Taxable Income is subject to Corporate Tax at 0%.
2. The portion of Taxable Income exceeding AED 375,000 is subject to Corporate Tax at 9%.

In your case, the Taxable Income of AED 500,000 means:
- The first AED 375,000 incurs no tax.
- The remaining AED 125,000 (which is AED 500,000 - AED 375,000) will be taxed at 9%.

Thus, you will owe Corporate Tax on the portion exceeding AED 375,000. 

Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 84 [example] (rerank -2.7262, compressed 71→13 sentences) Statements show an Accounting Income of AED 10,000,000. C LLC also has carried forward Tax Losses of AED 2,000,000. • Dividends received from UAE Resident companies: AED 1,000,000; • Income from its Foreign Permanent Establishment in Country B: AED 1,500,000; • Net Interest Expenditure: AED 7,000,00…
- [rank 2] page 21 [example] (rerank -3.4934, compressed 112→11 sentences) LLC generated Revenue of AED 8 million and incurred expenses of AED 2 million, resulting in a net profit of AED 6 million per its Financial Statements. For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period.…
- [rank 3] page 114 [example] (rerank -3.5888, compressed 242→12 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that woul…
- [rank 4] page 68 [example] (rerank -3.9891, compressed 41→17 sentences) C LLC has Revenue of AED 150,000,000, adjusted EBITDA of AED 130,000,000 and Profit Before Tax of AED 60,000,000 for its Financial Year ending 31 December 2025. In 2025, C LLC incurs costs including Interest expenditure of AED 80,000,000. C LLC also receives Interest income of AED 30,000,000, result…
- [rank 5] page 38 [example] (rerank -4.8378, compressed 248→6 sentences) During the Tax Period it has a total Revenue of AED 80,000,000. During the Tax Period, it undertakes a small number of transactions with individuals and earns AED 4,500,000 of Revenue. The remaining AED 75,500,000 meets the requirements to be considered as Qualifying Income. As transactions with ind…

## Q17 — Trap / out-of-scope
**Question:** How much VAT do I charge my customers?

**Query variants:**
- What is the applicable Value Added Tax rate that should be levied on transactions with clients?
- What is the prescribed VAT percentage that must be imposed on customer sales?
- What is the statutory rate of Value Added Tax to be applied in billing customers?

**Tokens in context:** 228

**Answer:** This is not covered in the provided document.  
Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 4 [prose] (rerank -9.0373, compressed 18→4 sentences) Corporate Tax rates for Qualifying Free Zone Persons Withholding Tax rate General Corporate Tax Guide | Corporate Tax | CTGGCT1 Tax Returns and payments
- [rank 2] page 4 [prose] (rerank -9.1788, compressed 18→7 sentences) Taxation of partnership and their partners Requirements to form a Tax Group Compliance with Corporate Tax requirements 9. How is any Corporate Tax liability calculated? Applicable Corporate Tax rates General tax rates Corporate Tax rates for Qualifying Free Zone Persons
- [rank 3] page 2 [prose] (rerank -9.3081, compressed 18→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Election to be taxed at the general rates of Corporate Tax 6. What is subject to Corporate Tax?
- [rank 4] page 72 [example] (rerank -10.163, compressed 127→3 sentences) Amounts withdrawn from the Business by a natural person who is a Taxable Recoverable input VAT;200 Value of the service or benefit provided by the Connected Person, and where the payment or benefit is incurred wholly and exclusively for the purposes of the Taxable
- [rank 5] page 38 [example] (rerank -10.4426, compressed 248→3 sentences) Activity and will be required to register for Corporate Tax.75 Revenue, it will be required to register with the FTA for Corporate Tax.77 Corporate Tax.

## Q18 — Trap / out-of-scope
**Question:** What's the corporate tax rate in Saudi Arabia?

**Query variants:**
- What is the applicable corporate tax rate imposed on entities operating within the jurisdiction of Saudi Arabia?
- Could you provide the current statutory corporate tax rate applicable to corporations in Saudi Arabia?
- What is the prevailing corporate tax rate for businesses registered in the Kingdom of Saudi Arabia?

**Tokens in context:** 1035

**Answer:** This is not covered in the provided document. Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 20 [prose] (rerank -1.4056, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…
- [rank 2] page 13 [prose] (rerank -2.5481, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…
- [rank 3] page 4 [prose] (rerank -2.6168, compressed 18→6 sentences) Corporate Tax rates for Qualifying Free Zone Persons Withholding Tax rate General Corporate Tax Guide | Corporate Tax | CTGGCT1 Requirements for the Withholding Tax Credit Foreign Tax Credit Administration of Corporate Tax
- [rank 4] page 19 [prose] (rerank -3.4959, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Corporate Tax Law Implementing Decisions on the Ministry of Finance and FTA websites Corporate Tax FTA Decisions on the FTA website General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter…
- [rank 5] page 111 [example] (rerank -4.497, compressed 84→20 sentences) Example 35: Application of Corporate Tax rates to Tax Groups If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Corporate Tax Payable (AED) Total Corporate Tax due per company Total Cor…

## Q19 — Trap / out-of-scope
**Question:** How do I lower the income tax taken from my salary in the UAE?

**Query variants:**
- What measures may be undertaken to mitigate the income tax liability associated with my remuneration in the UAE?
- What strategies are available to minimize the taxable income derived from my salary within the jurisdiction of the UAE?
- What avenues exist for the reduction of income tax obligations pertaining to my earnings in the United Arab Emirates?

**Tokens in context:** 1501

**Answer:** This is not covered in the provided document.  
Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 114 [example] (rerank -1.7123, compressed 242→16 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that woul…
- [rank 2] page 84 [example] (rerank -2.7383, compressed 71→14 sentences) Example 24: Calculation of Taxable Income Statements show an Accounting Income of AED 10,000,000. C LLC also has carried forward Tax Losses of AED 2,000,000. • Dividends received from UAE Resident companies: AED 1,000,000; • Income from its Foreign Permanent Establishment in Country B: AED 1,500,000…
- [rank 3] page 56 [example] (rerank -3.5485, compressed 47→4 sentences) 50% of F LLC, a UAE resident company. During the Tax Period, F LLC paid C LLC AED As dividends received from UAE Resident Persons are exempt from Corporate Tax, this amount should be excluded when calculating Taxable Income. C LLC’s Taxable Income (assuming no other adjustments), is therefore AED 7,…
- [rank 4] page 21 [example] (rerank -3.7652, compressed 112→16 sentences) For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period. • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: AED 375,000 x 0% = AED0 • The portion of the Taxable income exceeding…
- [rank 5] page 38 [example] (rerank -3.7693, compressed 248→9 sentences) During the Tax Period it has a total Revenue of AED 80,000,000. During the Tax Period, it undertakes a small number of transactions with individuals and earns AED 4,500,000 of Revenue. The UAE Constitution considers the Natural Resources in each Emirate to be the public property of that Emirate, and…

## Q20 — Trap / out-of-scope
**Question:** Exactly what penalty in AED will I get for filing 47 days late?

**Query variants:**
- What is the specific monetary penalty, expressed in AED, that will be imposed for a late filing of 47 days?
- What is the exact financial sanction in AED applicable for the submission of tax documents 47 days past the due date?
- What is the determined penalty amount in AED for the late filing of 47 days in accordance with the UAE Corporate Tax regulations?

**Tokens in context:** 872

**Answer:** For filing a Tax Return late, the penalty is AED 500 for each month of delay, or part thereof, for the first twelve months. Since 47 days is more than one month but less than two months, you will incur a penalty of AED 500. 

Source: page 114 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 80 [example] (rerank -8.5156, compressed 84→12 sentences) In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. • In the Tax Period ending on 31 December 2027, C LLC has Taxable Income of AED This means that C LLC must pay Corporate Tax of AED 78,750 (AED 375,000 x 0% + AED 875,000 x 9%). C LLC will have Tax Losses of AED 2,250,00…
- [rank 2] page 111 [example] (rerank -8.7307, compressed 84→6 sentences) Taxable Income (AED) Corporate Tax Payable (AED) Income of AED 15,000,000 would be AED 1,316,250. Taxable Income (AED) Corporate Tax Payable (AED) 0% rate on their first AED 375,000 of Taxable Income that is not Qualifying Income.
- [rank 3] page 89 [example] (rerank -8.8395, compressed 66→3 sentences) At the beginning of the Tax Period, C LLC had unutilised Tax Losses of AED 400,000. 89 of AED 400,000 brought forward from the prior Tax Period, subject to the 75% utilisation restriction. Should there be any remaining Taxable Income following the utilisation of the available Tax Losses, any Taxable…
- [rank 4] page 114 [example] (rerank -8.9987, compressed 242→13 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. The surplus amount (AED 300,000 – AED 135,000 = AED 165,000) cannot be carried forward or bac…
- [rank 5] page 20 [prose] (rerank -9.2469, compressed 7→4 sentences) 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 9% (nine percent) on the portion of the Taxable Income exceeding AED
