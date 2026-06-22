# Ring 4 RAG — results to grade

Config: embed=text-embedding-3-large, gen=gpt-4o, reranker=BAAI/bge-reranker-v2-m3, parent=2000, child=300, cosine_k=30, rerank_k=5, variants=3, hyde=ON, verify=ON, compress_prose=0.28/example=0.4, max_sents=20, token_budget=3500, pysbd=True

> **Grading tip (from Ring 1):** For each wrong answer, check the retrieved parents. If the correct page appears in rank 1-5 but the answer is wrong → **GENERATION failure** (prompt/model issue). If the correct page is missing entirely → **RETRIEVAL failure** (chunking/embedding/reranking issue). Tag each Q before running the evaluator.

## Q1 — Simple lookup
**Question:** What's the corporate tax rate in the UAE?

**HyDE hypothesis:** The corporate tax rate in the United Arab Emirates is set at a standard rate of 9% on taxable income exceeding AED 375,000, effective for financial years commencing on or after June 1, 2023. Entities with taxable income at or below this threshold are subject to a zero percent tax rate. Compliance with the provisions outlined in the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses is mandatory for all qualifying entities.

**Query variants:**
- What is the applicable corporate tax rate established under the UAE tax legislation?
- Could you specify the prevailing corporate tax rate as delineated in the UAE's fiscal regulations?
- What is the statutory corporate tax rate imposed by the United Arab Emirates tax framework?

**Tokens in context:** 2032
**Verification modified answer:** True

**Draft answer:** The corporate tax rate in the UAE is structured as follows: The first AED 375,000 of Taxable Income is subject to a 0% Corporate Tax rate. Any portion of the Taxable Income exceeding AED 375,000 is subject to a 9% Corporate Tax rate. Additionally, a 0% rate applies to Qualifying Income earned by certain Free Zone entities known as Qualifying Free Zone Persons. Source: page 21 of CTGGCT1.

**Final answer:** The corporate tax rate in the UAE is structured as follows: The first AED 375,000 of Taxable Income is subject to a 0% Corporate Tax rate. Any portion of the Taxable Income exceeding AED 375,000 is subject to a 9% Corporate Tax rate. Additionally, a 0% rate applies to Qualifying Income earned by certain Free Zone entities known as Qualifying Free Zone Persons. 

Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank 0.9694, compressed 112→20 sentences) • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: • The portion of the Taxable income exceeding AED 375,000 will be subject to Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x A LLC’s UAE Corporate Tax liability for the Tax Period will be AED …
- [rank 2] page 114 [example] (rerank 0.7215, compressed 242→20 sentences) At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that would have been paid in the UAE on the foreign income (AED 1,500,000 x 9% = AED The amount of Corporate Tax due is therefore AED 1…
- [rank 3] page 80 [example] (rerank 0.5903, compressed 84→20 sentences) C LLC is a UAE resident company. In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. LLC has Taxable Income of AED 5,000,000 per year. • In the Tax Period ending on 31 December 2027, C LLC has Taxable Income of AED This means that the maximum Tax Loss that can be used to …
- [rank 4] page 13 [prose] (rerank 0.576, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…
- [rank 5] page 111 [example] (rerank 0.5636, compressed 84→20 sentences) Example 35: Application of Corporate Tax rates to Tax Groups If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Corporate Tax Payable (AED) Total Corporate Tax due per company Taxable I…

## Q2 — Simple lookup
**Question:** When did corporate tax actually start in the UAE?

**HyDE hypothesis:** The implementation of corporate tax in the United Arab Emirates commenced on June 1, 2023, as stipulated in Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses. This legislation introduced a federal corporate tax framework applicable to taxable persons, establishing a standard rate of 9% on profits exceeding AED 375,000, thereby aligning the UAE's tax regime with international standards.

**Query variants:**
- What is the commencement date of the corporate tax regime in the United Arab Emirates?
- At what point in time did the implementation of corporate taxation begin within the UAE jurisdiction?
- Can you specify the effective date of the corporate tax legislation in the United Arab Emirates?

**Tokens in context:** 1497
**Verification modified answer:** False

**Final answer:** Corporate tax in the UAE applies to tax periods commencing on or after 1 June 2023. Source: page 13 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 13 [prose] (rerank 0.7755, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…
- [rank 2] page 21 [example] (rerank 0.0809, compressed 112→20 sentences) • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x A LLC’s UAE Corporate Tax liability for the Tax Period will be AED 506,250. In order to calculate its UAE Corporate Tax payable, A LLC will need…
- [rank 3] page 18 [prose] (rerank 0.051, compressed 25→13 sentences) Corporations and Businesses is referred to as “FTA Decision No. 5 of 2023”; Federal Tax Authority Decision No. 6 of 2023 on Tax Deregistration Timeline for the Purposes of Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses is referred to as “FTA Decision No. 6 of 2023”;…
- [rank 4] page 19 [prose] (rerank 0.0459, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Corporate Tax FTA Decisions on the FTA website General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter sets out a brief overview of the core principles of Corporate Tax and how the Corpor…
- [rank 5] page 53 [example] (rerank 0.0377, compressed 24→6 sentences) During the Financial Year ending 31 December 2025, S LLC, a UAE resident company, recognised a revaluation loss in its Financial Statements in respect of an asset measured at fair value. Several exemptions are provided for within the Corporate Tax regime.135 135 Articles 22 to 25 of the Corporate Ta…

## Q3 — Simple lookup
**Question:** How much profit can I make before I owe any corporate tax?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, a taxable person is subject to corporate tax on profits exceeding AED 375,000. Profits up to this threshold are exempt from corporate tax liability, thereby establishing a de minimis threshold for taxable income. Any profits generated beyond this amount will be subject to the applicable corporate tax rate as stipulated in the relevant regulations.

**Query variants:**
- What is the threshold of taxable profit that must be exceeded before corporate tax liabilities are incurred?
- What is the maximum allowable profit exempt from corporate taxation prior to the imposition of tax obligations?
- At what level of net profit does the obligation to remit corporate tax arise under the applicable regulations?

**Tokens in context:** 1110
**Verification modified answer:** False

**Final answer:** The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%, meaning you can make up to AED 375,000 in profit before owing any corporate tax. Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank 0.1056, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax A LLC’s Taxable Income for its Tax Period will be the accounting net profit (or loss) of the business, after making tax adjustments for certain items specified in the Corporate For the purposes of this example, A LLC does not need to make any tax adjustments, …
- [rank 2] page 20 [prose] (rerank 0.0394, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…
- [rank 3] page 87 [example] (rerank 0.0233, compressed 39→7 sentences) As a result, G LLC will only need to recognise, for Corporate Tax purposes, a gain of General Corporate Tax Guide | Corporate Tax | CTGGCT1 This chapter provides an overview of the reliefs available under the Corporate Tax Corporate Tax burden and compliance costs in the Corporate Tax regime, primar…
- [rank 4] page 101 [example] (rerank 0.0167, compressed 174→20 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 (c) of the Corporate Tax Law. General Corporate Tax Guide | Corporate Tax | CTGGCT1 317 Article 40(1) of the Corporate Tax Law. General Corporate Tax Guide | Corporate Tax | CTGGCT1 (c) of the Corporate Tax Law. 329 Article 41(1) of the Corporate…
- [rank 5] page 6 [prose] (rerank 0.0105, compressed 15→10 sentences) Corporate Tax: The tax imposed by the Corporate Tax Law on juridical persons and Business income. Corporate Tax Law: Federal Decree Law No. 47 of 2022 on the Taxation of Corporations and Businesses. Corporate Tax Payable: Corporate Tax that has or will become due for payment to the FTA in respect of…

## Q4 — Simple lookup
**Question:** After my financial year ends, how long do I have to file my return?

**HyDE hypothesis:** Pursuant to Article 51 of the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses, a taxable person is required to submit their corporate tax return within nine months following the end of their financial year. Failure to comply with this deadline may result in penalties as stipulated under the relevant provisions of the law.

**Query variants:**
- What is the prescribed timeframe for the submission of my tax return subsequent to the conclusion of my financial year?
- What is the statutory deadline for filing my tax return following the termination of my financial reporting period?
- How long is the allowable period for the filing of my tax return after the end of my fiscal year?

**Tokens in context:** 292
**Verification modified answer:** False

**Final answer:** After your financial year ends, you have 9 months to file your tax return. Source: page 83 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 19 [prose] (rerank 0.1326, compressed 30→8 sentences) Corporate Tax Law Corporate Tax FAQs Corporate Tax is paid on an annual basis with reference to the Tax Period of a Taxable A Tax Period is the Financial Year or part thereof for which a Tax Return needs to be filed. The Financial Year is the period of 12 months for which Financial Payment of Corpor…
- [rank 2] page 83 [example] (rerank 0.1006, compressed 28→3 sentences) Determination of Taxable Income Taxable Persons have to submit a Tax Return to the FTA within 9 months after the end of each Tax Period.240 The Tax Return is self-assessed, and Taxable Persons must provide their Accounting
- [rank 3] page 7 [prose] (rerank 0.0104, compressed 15→3 sentences) Corporate Tax Law. General Corporate Tax Guide | Corporate Tax | CTGGCT1 Financial Year: The Gregorian calendar year, or the twelve-month period for which the Taxable Person prepares Financial Statements.
- [rank 4] page 53 [example] (rerank 0.0035, compressed 24→3 sentences) The asset has not been sold at the end of the Tax Period. Several exemptions are provided for within the Corporate Tax regime.135 General Corporate Tax Guide | Corporate Tax | CTGGCT1
- [rank 5] page 14 [prose] (rerank 0.003, compressed 20→3 sentences) Person’s Corporate Tax liability is calculated. Corporate Tax administration process, from Tax Registration and record keeping to submitting returns and making payments. Corporate Tax regime function.

## Q5 — Conditional
**Question:** My free-zone company made AED 2 million profit — do I pay 0%?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, a free zone entity may be eligible for a 0% corporate tax rate on qualifying income, provided it meets the specific criteria outlined in the relevant regulations. However, it is imperative to ensure compliance with the economic substance requirements and any applicable licensing conditions to maintain this preferential tax treatment. Therefore, while a profit of AED 2 million may be subject to a 0% tax rate, the entity must verify its adherence to all regulatory stipulations to confirm its eligibility.

**Query variants:**
- Does the profit of AED 2 million generated by my free-zone enterprise render it subject to a 0% corporate tax rate?
- Is my free-zone company, having realized a profit of AED 2 million, exempt from corporate taxation at a rate of 0%?
- In light of my free-zone company's profit of AED 2 million, am I liable for corporate tax at a rate of 0%?

**Tokens in context:** 1659
**Verification modified answer:** True

**Draft answer:** The Corporate Tax rate for a Qualifying Free Zone Person depends on whether the income is considered Qualifying Income. If your free-zone company qualifies as a Qualifying Free Zone Person and the AED 2 million profit is considered Qualifying Income, then it would be subject to a 0% Corporate Tax rate. However, if the income is not Qualifying Income, the standard 9% Corporate Tax rate would apply, and unlike ordinary Taxable Persons, Qualifying Free Zone Persons are not entitled to a 0% rate on their first AED 375,000 of Taxable Income that is not Qualifying Income. 

Source: page 111 of CTGGCT1.

**Final answer:** The Corporate Tax rate for a Qualifying Free Zone Person depends on whether the income is considered Qualifying Income. If your free-zone company qualifies as a Qualifying Free Zone Person and the profit is considered Qualifying Income, then it would be subject to a 0% Corporate Tax rate. However, if the income is not Qualifying Income, the standard 9% Corporate Tax rate would apply, and unlike ordinary Taxable Persons, Qualifying Free Zone Persons are not entitled to a 0% rate on their first AED 375,000 of Taxable Income that is not Qualifying Income.

Source: page 111 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank 0.8017, compressed 112→18 sentences) LLC generated Revenue of AED 8 million and incurred expenses of AED 2 million, resulting in a net profit of AED 6 million per its Financial Statements. For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period.…
- [rank 2] page 111 [example] (rerank 0.7129, compressed 84→20 sentences) If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Corporate Tax Payable (AED) Income of AED 15,000,000 would be AED 1,316,250. Taxable Income (AED) Corporate Tax Payable (AED) Corporat…
- [rank 3] page 80 [example] (rerank 0.3499, compressed 84→16 sentences) C LLC is a UAE resident company. In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. LLC has Taxable Income of AED 5,000,000 per year. • In the Tax Period ending on 31 December 2027, C LLC has Taxable Income of AED This means that the maximum Tax Loss that can be used to …
- [rank 4] page 20 [prose] (rerank 0.3069, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…
- [rank 5] page 38 [example] (rerank 0.0832, compressed 248→10 sentences) H LLC is a Free Zone Person that sells vehicles to other Free Zone Persons. During the Tax Period it has a total Revenue of AED 80,000,000. H LLC maintains adequate substance in the Free Zone, has not made an election to be subject to UAE Corporate During the Tax Period, it undertakes a small number…

## Q6 — Conditional
**Question:** My business is tiny with very low revenue. Is there relief so I pay nothing?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, specifically Article 5, businesses with an annual revenue not exceeding AED 375,000 are exempt from corporate tax obligations. This threshold is established to provide relief to small enterprises, thereby ensuring that entities with minimal economic activity are not subject to tax liabilities. It is imperative for businesses to maintain accurate financial records to substantiate their revenue levels and eligibility for this exemption.

**Query variants:**
- Is there a provision for tax relief applicable to small enterprises with minimal revenue that would exempt them from corporate tax obligations?
- What mechanisms exist within the corporate tax framework to provide relief for businesses with negligible revenue, potentially resulting in a zero tax liability?
- Can small businesses with limited income qualify for any exemptions or relief measures that would alleviate their corporate tax responsibilities?

**Tokens in context:** 467
**Verification modified answer:** False

**Final answer:** If your business's revenue does not exceed the small business relief threshold of AED 3,000,000 per tax period, you may be eligible for small business relief. This relief is available to eligible UAE businesses and can reduce their taxable amount. However, a Qualifying Free Zone Person cannot claim small business relief. Additionally, if you elect to benefit from small business relief, you will not be required to maintain transfer pricing documentation for that tax period. For further details, you should consult Ministerial Decision No. 73 of 2023 on Small Business Relief and the Corporate Tax Guide on Small Business Relief. 

Source: page 87 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 89 [example] (rerank 0.1289, compressed 16→3 sentences) Example 27: Electing for small business relief To date, Mr X’s Revenue has never exceeded the small business relief threshold of AED 3,000,000 per Tax Mr X is eligible to benefit from small business relief as his Revenue for the 31 December
- [rank 2] page 89 [example] (rerank 0.0232, compressed 66→3 sentences) In the prior year, C LLC’s Revenue did not exceed the AED 3,000,000 relief threshold. C LLC elects for small business relief for the Tax Period ending 31 December 2025. In the Tax Period ending 31 December 2026, C LLC sold a factory to B LLC for AED 5 million, resulting in its Revenue exceeding the …
- [rank 3] page 87 [example] (rerank 0.0217, compressed 39→8 sentences) Small business relief Small business relief is provided to eligible UAE businesses, and reduces their Taxable Person has elected to benefit from small business relief, they will still be able to carry forward any unutilised Tax Losses 250  and disallowed Net Interest In addition, a Qualifying Free Z…
- [rank 4] page 16 [prose] (rerank 0.0119, compressed 18→3 sentences) Ministerial Decision No. 43 of 2023 Concerning Exception from Tax Registration for the Purpose of Federal Decree-Law No. 47 of 2022 on the Taxation of Business Activities Conducted by a Government Entity as a Single Taxable Ministerial Decision No. 73 of 2023 on Small Business Relief for the Purpose…
- [rank 5] page 93 [example] (rerank 0.0082, compressed 73→3 sentences) Business restructuring relief Business is transferred in exchange for shares or other ownership interests, business restructuring relief may apply to eliminate the Corporate Tax impact of these transactions. The relief is available where a Business is transferred in exchange for ownership interests …

## Q7 — Conditional
**Question:** My profit is below the threshold — do I still have to register at all?

**HyDE hypothesis:** Entities whose taxable income falls below the prescribed threshold are not required to register for corporate tax purposes; however, they may opt to voluntarily register. It is imperative to maintain accurate financial records to substantiate the income levels and ensure compliance with any applicable regulatory obligations, including the submission of annual financial statements, if required.

**Query variants:**
- Is registration mandated for entities whose profits fall below the established threshold?
- Are entities with profits under the prescribed threshold required to complete the registration process?
- Must an entity with profits that do not meet the threshold criteria still fulfill the registration obligations?

**Tokens in context:** 347
**Verification modified answer:** False

**Final answer:** If your profit is below the threshold, you may still be required to register for Corporate Tax if your revenue from transactions exceeds certain thresholds. For example, if your revenue from transactions with individuals exceeds the de minimis threshold of AED 4,000,000, you will be required to register with the Federal Tax Authority (FTA) for Corporate Tax. However, if your revenue does not exceed the small business relief threshold of AED 3,000,000, you may be eligible for small business relief and not required to register. 

Source: page 38 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 89 [example] (rerank 0.0055, compressed 16→3 sentences) To date, Mr X’s Revenue has never exceeded the small business relief threshold of AED 3,000,000 per Tax Mr X is eligible to benefit from small business relief as his Revenue for the 31 December 2025 Tax Period does not exceed AED 3,000,000, which is also the case for previous years’ Tax Periods.
- [rank 2] page 38 [example] (rerank 0.0034, compressed 248→3 sentences) As transactions with individuals are generally Excluded Activities, and Revenue from these sales exceeded the de minimis threshold of AED 4,000,000 (being the lower of Activity and will be required to register for Corporate Tax.75 Revenue, it will be required to register with the FTA for Corporate T…
- [rank 3] page 2 [prose] (rerank 0.0018, compressed 18→9 sentences) Qualifying Activities The de minimis requirement Election to be taxed at the general rates of Corporate Tax Automatically Exempt Persons Exempt Persons if they notify the Ministry, and meet relevant conditions Registration and record keeping obligations of Exempt Persons 6. What is subject to Corpor…
- [rank 4] page 14 [prose] (rerank 0.0011, compressed 20→3 sentences) Person’s Corporate Tax liability is calculated. Corporate Tax administration process, from Tax Registration and record keeping to submitting returns and making payments. Corporate Tax regime function.
- [rank 5] page 19 [prose] (rerank 0.0006, compressed 30→8 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Tax’ or ‘Business Profits Tax’ in other jurisdictions. Corporate Tax is charged on a wide range of Business profits, and those subject to How does Corporate Tax work? Taxable Persons are subject to Corporate Tax on their Tax…

## Q8 — Conditional
**Question:** I personally earn rent from a flat I own. Is that taxed?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, rental income derived from the ownership of real estate is subject to taxation if the individual is engaged in a business activity related to the leasing of properties. However, if the rental income is classified as personal income and not part of a business operation, it may be exempt from corporate tax, provided that the individual does not exceed the stipulated threshold for taxable income as defined by the relevant regulations. It is advisable to consult the specific guidelines to determine the applicability of tax obligations in such cases.

**Query variants:**
- Does the income derived from rental properties owned by an individual constitute taxable income under the UAE Corporate Tax framework?
- Is the rental income generated from a personally owned residential property subject to taxation in accordance with UAE Corporate Tax regulations?
- Is the revenue obtained from leasing a privately owned flat liable for taxation under the provisions of the UAE Corporate Tax law?

**Tokens in context:** 342
**Verification modified answer:** False

**Final answer:** If you earn rent from a flat you own, it is considered a Real Estate Investment activity. According to the context, any investment activity conducted by a natural person related to the leasing, sub-leasing, and renting of real estate property in the UAE is considered a Real Estate Investment. This activity does not require a license from a Licensing Authority. Therefore, the income you earn from renting out your flat would be subject to Corporate Tax as it is considered business income. 

Source: page 11 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 5 [prose] (rerank 0.0044, compressed 18→3 sentences) Person recognises income when earned and expenditure when incurred. Commercial Property: Immovable Property or part thereof: Business income.
- [rank 2] page 11 [prose] (rerank 0.0036, compressed 14→4 sentences) Real Estate Investment: Any investment activity conducted by a natural person related to, directly or indirectly, the sale, leasing, sub-leasing, and renting of land or real estate property in the UAE that is not conducted, or does not require to be conducted through a Licence from a Licensing Autho…
- [rank 3] page 20 [prose] (rerank 0.003, compressed 7→3 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 9% (nine percent) on the portion of the Taxable Income exceeding AED
- [rank 4] page 2 [prose] (rerank 0.0027, compressed 19→9 sentences) 5. Who is subject to Corporate Tax? Taxable Persons Resident Taxable Persons Impact of Double Taxation Agreements on Resident Taxable Persons Non-Resident Taxable Persons Non-Resident Person that derives State Sourced Income Non-resident juridical person that has a nexus in the UAE (derives income f…
- [rank 5] page 12 [prose] (rerank 0.0026, compressed 23→3 sentences) State Sourced Income: Income accruing in, or derived from, the UAE as specified in Tax purposes with the FTA. Taxable Income: The income that is subject to Corporate Tax under the Corporate

## Q9 — Multi-hop
**Question:** As a free-zone company, what exactly counts as 'qualifying income' for the 0%?

**HyDE hypothesis:** Under the UAE Corporate Tax regime, 'qualifying income' for free-zone companies refers to income derived from activities conducted within the designated free zone, including but not limited to, trading, manufacturing, and service provision to non-resident entities. Additionally, income generated from specific financial services, intellectual property rights, and certain qualifying investments may also be classified as qualifying income, provided that such activities comply with the regulatory requirements stipulated in the relevant free zone authority's framework. It is imperative that free-zone companies maintain adequate documentation to substantiate the nature and source of their income to ensure eligibility for the 0% corporate tax rate.

**Query variants:**
- What constitutes 'qualifying income' eligible for the 0% tax rate for entities operating within a free-zone jurisdiction?
- In the context of a free-zone entity, what specific revenue streams are classified as 'qualifying income' for the application of the 0% corporate tax rate?
- Could you delineate the parameters that define 'qualifying income' for the purpose of the 0% taxation applicable to free-zone companies?

**Tokens in context:** 1151
**Verification modified answer:** True

**Draft answer:** For a Free Zone company, 'Qualifying Income' eligible for the 0% Corporate Tax rate includes income derived by a Qualifying Free Zone Person from activities determined by a decision issued by the Minister. Specifically, income from transactions between Free Zone Persons related to Commercial Property in a Free Zone is considered Qualifying Income. However, income derived from Commercial Property transactions with a Person who is not a Free Zone Person, or from residential and other non-Commercial Property located in a Free Zone, is not considered Qualifying Income and is subject to the standard 9% Corporate Tax rate. Source: page 38 of CTGGCT1.

**Final answer:** For a Free Zone company, 'Qualifying Income' eligible for the 0% Corporate Tax rate includes income derived by a Qualifying Free Zone Person from activities determined by a decision issued by the Minister. Specifically, income from transactions between Free Zone Persons related to Commercial Property in a Free Zone is considered Qualifying Income. However, income derived from Commercial Property transactions with a Person who is not a Free Zone Person, or from residential and other non-Commercial Property located in a Free Zone, is treated as regular Taxable Income and is subject to the standard 9% Corporate Tax rate. Source: page 38 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 38 [example] (rerank 0.8849, compressed 7→6 sentences) Example 4: Qualifying Income F LLC and G LLC are both Free Zone Persons. F LLC (a Qualifying Free Zone Person) owns a number of warehouses located in a Free Zone. As the transaction is between two Free Zone Persons, and the sale relates to Commercial Property in a Free Zone, the income earned on the…
- [rank 2] page 111 [example] (rerank 0.582, compressed 84→20 sentences) If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Taxable Income (AED) Corporate Tax rates for Qualifying Free Zone Persons Corporate Tax applies to Qualifying Free Zone Persons at the…
- [rank 3] page 37 [example] (rerank 0.4023, compressed 9→3 sentences) E LLC is a Free Zone Person, and generates all of its income from leasing a property which is not located in a Free Zone. As this is Revenue from an Excluded Activity, this income is not Qualifying Income. As E LLC only earns non-qualifying Revenue, it will not satisfy the de minimis requirement and…
- [rank 4] page 10 [prose] (rerank 0.093, compressed 16→10 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Personal Investment: Investment activity that a natural person conducts for their personal account that is neither conducted through a Licence or requiring a Licence from a Licensing Authority in the UAE, nor considered as a commercial business i…
- [rank 5] page 7 [prose] (rerank 0.0721, compressed 15→9 sentences) and conducted by a Qualifying Free Zone Person from which non-Qualifying Income is derived. Exempt Person: A Person exempt from Corporate Tax under Article 4 of the Corporate Tax Law. Extractive Business: The Business or Business Activity of exploring, extracting, removing, or otherwise producing an…

## Q10 — Multi-hop
**Question:** Can my group of companies be taxed as one, and what must we meet?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, a group of companies may elect to be treated as a single taxable entity, provided that they meet the criteria for group taxation as stipulated in Article X of the Law. Specifically, the companies must be wholly owned by the same ultimate parent entity, maintain a consolidated financial statement, and comply with any additional regulatory requirements set forth by the Federal Tax Authority.

**Query variants:**
- Is it permissible for my corporate group to be treated as a single taxable entity, and what criteria must be satisfied to achieve this status?
- Can my consortium of enterprises be consolidated for taxation purposes, and what requirements must be fulfilled to qualify for such treatment?
- Is it allowable for my affiliated companies to be assessed as a unified taxable group, and what conditions must be met to obtain this designation?

**Tokens in context:** 1352
**Verification modified answer:** False

**Final answer:** Yes, your group of companies can be taxed as one by forming a Tax Group. To do so, the group must meet the ownership requirements as specified in the Corporate Tax Law. Specifically, a Parent Company must hold the necessary ownership in the other companies within the group. Once these conditions are met, an application to form a Tax Group can be submitted to the Federal Tax Authority (FTA). Upon approval, the group will be treated as a single Taxable Person for Corporate Tax purposes. 

Source: page 107 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 107 [example] (rerank 0.107, compressed 87→20 sentences) Example 34: Formation of a Tax Group C LLC, therefore, meets the ownership requirements of F LLC and Z LLC in order to form a Tax C LLC (as the Parent Company), F LLC and Z LLC made an application to form a Tax Group, effective from the Tax Period beginning 1 September 2026. The application to form …
- [rank 2] page 4 [prose] (rerank 0.0217, compressed 18→15 sentences) Business restructuring relief Taxation of partnership and their partners Unincorporated Partnerships Incorporated partnerships Tax treatment of a foreign partnership Tax Group regime Requirements to form a Tax Group Formation and cessation of a Tax Group Joining or leaving a Tax Group Compliance wit…
- [rank 3] page 111 [example] (rerank 0.0088, compressed 84→16 sentences) Example 35: Application of Corporate Tax rates to Tax Groups If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Total Corporate Tax due per company Total Corporate Tax Payable for all three companies If the…
- [rank 4] page 12 [prose] (rerank 0.0048, compressed 23→15 sentences) Article 13 of the Corporate Tax Law. Partnership Capital, as applicable, is held by a Parent Company, in accordance with Article 40(1) of the Corporate Tax Law. Tax Deregistration: A procedure under which a Person is deregistered for Corporate Tax purposes with the FTA. Tax Group: Two or more Taxabl…
- [rank 5] page 38 [example] (rerank 0.0028, compressed 248→20 sentences) These types of entities are treated the same as any other juridical person, with their income being within the scope of Corporate Tax. General Corporate Tax Guide | Corporate Tax | CTGGCT1 Therefore, entities that are considered as “Family Foundations” for Corporate Tax purposes can, subject to meet…

## Q11 — Multi-hop
**Question:** My business made a loss last year — can I use it to cut this year's tax?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, specifically Article [insert relevant article number], a business that incurs a tax loss in a given financial year may carry forward such losses to offset taxable income in subsequent financial years, subject to the limitations and conditions prescribed therein. It is imperative that the loss is properly documented and reported in accordance with the applicable accounting standards to ensure eligibility for carryforward against future taxable profits.

**Query variants:**
- Is it permissible to apply the prior year's fiscal loss to offset the current tax liability?
- Can the losses incurred in the preceding fiscal year be utilized to reduce the taxable income for the current year?
- Am I entitled to carry forward the operational losses from the previous year to mitigate this year's tax obligations?

**Tokens in context:** 790
**Verification modified answer:** True

**Draft answer:** Yes, you can use last year's Tax Loss to offset this year's Taxable Income, subject to certain conditions. The maximum Tax Loss that can be used to offset against your Taxable Income is 75% of the Taxable Income for the current year. Additionally, the owners of the business must have continuously held at least 50% ownership from the start of the period in which the loss was incurred to the end of the Tax Period in which the Tax Loss is used. If there is a change in ownership of more than 50%, the Tax Losses can still be carried forward provided the same or similar business is carried on following the change in ownership. Source: page 80 of CTGGCT1.

**Final answer:** The draft answer contains a factual claim that is not fully supported by the context. The claim regarding the maximum Tax Loss that can be used to offset against Taxable Income being 75% of the Taxable Income for the current year is not explicitly stated in the provided context. The context mentions that the maximum Tax Loss that can be used to offset against Taxable Income is AED 5,000,000 x 75% = AED 3,750,000, but it does not generalize this to all Taxable Income.

Here is the corrected answer:

Yes, you can use last year's Tax Loss to offset this year's Taxable Income, subject to certain conditions. Additionally, the owners of the business must have continuously held at least 50% ownership from the start of the period in which the loss was incurred to the end of the Tax Period in which the Tax Loss is used. If there is a change in ownership of more than 50%, the Tax Losses can still be carried forward provided the same or similar business is carried on following the change in ownership. Source: page 80 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 89 [example] (rerank 0.2251, compressed 66→4 sentences) Example 28: Carried forward unutilised Tax Losses when electing for small business relief At the beginning of the Tax Period, C LLC had unutilised Tax Losses of AED 400,000. LLC’s carried forward Tax Losses cannot be used in this Tax Period, but can be carried forward and used in future Tax Periods …
- [rank 2] page 80 [example] (rerank 0.0653, compressed 84→20 sentences) Example 22: Carried forward Tax Losses In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. • In the Tax Period ending on 31 December 2026, C LLC makes a Tax Loss and there are no amounts to be taxed. This means that the maximum Tax Loss that can be used to offset against …
- [rank 3] page 3 [prose] (rerank 0.0268, compressed 15→8 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Tax Losses Tax Loss relief Tax Losses and change of ownership Transfer of Tax Losses Determination of Taxable Income Small business relief Business restructuring relief
- [rank 4] page 83 [example] (rerank 0.0125, compressed 28→9 sentences) Example 23: Transfer of Tax Losses C LLC makes a loss of AED 2,000,000 and F LLC makes a profit of AED 2,000,000 in the same Tax Period. C LLC chooses to transfer AED 1,500,000 of Tax Losses to F The remaining AED 500,000 of unutilised losses is carried forward by C LLC to the subsequent Tax Period.…
- [rank 5] page 53 [example] (rerank 0.01, compressed 24→3 sentences) Several exemptions are provided for within the Corporate Tax regime.135 Income cannot be deducted for Corporate Tax purposes.136 Income will be deductible.

## Q12 — Multi-hop
**Question:** What records must I keep, and for how long, to stay compliant?

**HyDE hypothesis:** In accordance with the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses, taxpayers are required to maintain accurate and complete records of all transactions, including financial statements, invoices, and supporting documentation, for a minimum period of five years from the end of the relevant tax period. These records must be readily available for inspection by the Federal Tax Authority to ensure compliance with the provisions of the corporate tax regime.

**Query variants:**
- What documentation is required to be maintained, and for what duration, to ensure compliance with regulatory obligations?
- What records are mandated for retention, and what is the prescribed retention period to uphold compliance standards?
- Which specific records are necessary to be preserved, and what is the requisite timeframe for retention to achieve compliance?

**Tokens in context:** 256
**Verification modified answer:** False

**Final answer:** This is not covered in the provided document. Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 4 [prose] (rerank 0.009, compressed 18→3 sentences) Tax Returns and payments Record keeping How long should records be kept?
- [rank 2] page 2 [prose] (rerank 0.0059, compressed 18→3 sentences) Exempt Persons if they notify the Ministry, and meet relevant conditions Registration and record keeping obligations of Exempt Persons Tax Period
- [rank 3] page 7 [prose] (rerank 0.0021, compressed 15→3 sentences) Financial Statements: A complete set of statements as specified under the Accounting Standards applied by the Taxable Person, which includes, but is not limited to, statement of income, statement of other comprehensive income, balance sheet, statement of changes in equity and cash flow statement. Fi…
- [rank 4] page 13 [prose] (rerank 0.0017, compressed 20→3 sentences) The provisions of the Corporate Tax Law shall apply to Tax Periods commencing on or after 1 June 2023. • an overview of the main Corporate Tax rules and procedures, including the determination of the Corporate Tax base, the calculation of Corporate Tax, the filing of Corporate Tax Returns, and other…
- [rank 5] page 19 [prose] (rerank 0.0015, compressed 30→3 sentences) Explanatory Guide on Corporate Tax Law Corporate Tax FAQs A Tax Period is the Financial Year or part thereof for which a Tax Return needs to be filed.

## Q13 — Describe-your-business
**Question:** I freelance from home in Dubai with no trade licence — do I owe corporate tax?

**HyDE hypothesis:** Under the provisions of the UAE Corporate Tax Law, individuals engaging in freelance activities without a valid trade license are not recognized as conducting a formal business entity. Consequently, such individuals are not subject to corporate tax obligations. However, it is advisable to obtain the necessary trade license to ensure compliance with local regulations and to facilitate any potential tax liabilities that may arise from formalized business operations.

**Query variants:**
- Does my engagement in freelance activities from a residential location in Dubai, absent a trade license, render me liable for corporate tax obligations?
- Am I subject to corporate tax liabilities as a result of conducting freelance operations from my domicile in Dubai without possessing a trade license?
- Is there a corporate tax obligation applicable to my freelance activities conducted from home in Dubai in the absence of a valid trade license?

**Tokens in context:** 1957
**Verification modified answer:** False

**Final answer:** If you are a natural person conducting Business or Business Activities in the UAE and have a Turnover of over AED 1,000,000 per Gregorian calendar year from such activities, you may be subject to Corporate Tax. The Corporate Tax regime applies to natural persons based on their business connection to the UAE, regardless of whether they hold a residency visa or how much time they spend in the UAE. Therefore, if your freelance activities generate a Turnover exceeding this threshold, you would be subject to Corporate Tax. Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 26 [example] (rerank 0.0337, compressed 298→20 sentences) For natural persons, residence for Corporate Tax purposes is concerned with the person’s business connection to the UAE. It is this connection, rather than other factors such as nationality or where a person is physically present, that gives the UAE the powers to levy Corporate Tax on an individual’…
- [rank 2] page 21 [example] (rerank 0.0254, compressed 112→17 sentences) For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period. • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,0…
- [rank 3] page 19 [prose] (rerank 0.0201, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Corporate Tax Law Implementing Decisions on the Ministry of Finance and FTA websites Corporate Tax FTA Decisions on the FTA website General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter…
- [rank 4] page 12 [prose] (rerank 0.0152, compressed 23→15 sentences) State Sourced Income: Income accruing in, or derived from, the UAE as specified in Article 13 of the Corporate Tax Law. Article 40(1) of the Corporate Tax Law. Tax Deregistration: A procedure under which a Person is deregistered for Corporate Tax purposes with the FTA. Tax Loss: Any negative Taxable…
- [rank 5] page 13 [prose] (rerank 0.0138, compressed 20→12 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate General…

## Q14 — Describe-your-business
**Question:** I run a free-zone online store selling to mainland UAE customers — how am I taxed?

**HyDE hypothesis:** As a free zone entity engaged in e-commerce activities, your income derived from sales to mainland UAE customers is subject to the provisions of the UAE Corporate Tax Law. Specifically, while free zone businesses may benefit from a zero percent corporate tax rate on qualifying income, any income generated from activities conducted with mainland UAE customers may be subject to the standard corporate tax rate of 9% on taxable income exceeding AED 375,000, unless otherwise exempted under applicable regulations. It is imperative to ensure compliance with the relevant registration and reporting requirements as stipulated by the Federal Tax Authority.

**Query variants:**
- What are the tax implications for an online retail operation established in a free zone that transacts with customers located in mainland UAE?
- What is the applicable corporate tax regime for a free-zone e-commerce entity engaging in sales to consumers in the mainland UAE?
- Could you elucidate the taxation framework governing a free-zone online business that sells products to clients in the mainland UAE?

**Tokens in context:** 873
**Verification modified answer:** True

**Draft answer:** If you run a free-zone online store selling to mainland UAE customers, your tax obligations depend on whether you qualify as a Qualifying Free Zone Person. A Qualifying Free Zone Person is a Free Zone Person that meets the conditions of Article 18 of the Corporate Tax Law and is subject to Corporate Tax under Article 3(2) of the Corporate Tax Law. If your activities generate Qualifying Income, they will be subject to Corporate Tax at the rate specified in Article 3(2)(a) of the Corporate Tax Law. However, if your income is considered non-Qualifying Income, it may be subject to different tax treatments. It is important to determine whether your income from selling to mainland UAE customers is considered Qualifying or non-Qualifying Income to understand your specific tax obligations. 

Source: page 10 of CTGGCT1.

**Final answer:** If you run a free-zone online store selling to mainland UAE customers, your tax obligations depend on whether you qualify as a Qualifying Free Zone Person. A Qualifying Free Zone Person is a Free Zone Person that meets the conditions of Article 18 of the Corporate Tax Law and is subject to Corporate Tax under Article 3(2) of the Corporate Tax Law. If your activities generate Qualifying Income, they will be subject to Corporate Tax at the rate specified in Article 3(2) of the Corporate Tax Law. However, if your income is considered non-Qualifying Income, it may be subject to different tax treatments. It is important to determine whether your income from selling to mainland UAE customers is considered Qualifying or non-Qualifying Income to understand your specific tax obligations. 

Source: page 10 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 8 [prose] (rerank 0.1992, compressed 17→5 sentences) Free Zone: A designated and defined geographic area within the UAE that is specified in a decision issued by the Cabinet at the suggestion of the Minister. Free Zone Person: A juridical person incorporated, established, or otherwise registered in a Free Zone, including a branch of a Non-Resident Per…
- [rank 2] page 7 [prose] (rerank 0.1513, compressed 15→9 sentences) and conducted by a Qualifying Free Zone Person from which non-Qualifying Income is derived. Exempt Person: A Person exempt from Corporate Tax under Article 4 of the Corporate Tax Law. Extractive Business: The Business or Business Activity of exploring, extracting, removing, or otherwise producing an…
- [rank 3] page 38 [example] (rerank 0.1169, compressed 248→10 sentences) H LLC is a Free Zone Person that sells vehicles to other Free Zone Persons. During the Tax Period it has a total Revenue of AED 80,000,000. H LLC maintains adequate substance in the Free Zone, has not made an election to be subject to UAE Corporate During the Tax Period, it undertakes a small number…
- [rank 4] page 10 [prose] (rerank 0.0856, compressed 16→7 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Personal Investment: Investment activity that a natural person conducts for their personal account that is neither conducted through a Licence or requiring a Licence from a Licensing Authority in the UAE, nor considered as a commercial business i…
- [rank 5] page 54 [example] (rerank 0.0731, compressed 41→3 sentences) C LLC is a UAE resident company which sells food and drink products in the UAE and around the world. C LLC enters into many contracts with suppliers and customers, both in the UAE and at its Permanent Establishments around the world. This exemption also covers distributions made by a Resident Free Z…

## Q15 — Describe-your-business
**Question:** We're a 3-person startup with no profit yet. Any corporate tax obligations?

**HyDE hypothesis:** In accordance with the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses, entities with no taxable income are not subject to corporate tax obligations. However, it is imperative that the startup complies with the registration requirements and submits an annual tax return, even in the absence of profit, to ensure adherence to the regulatory framework established by the Federal Tax Authority.

**Query variants:**
- Is our three-member startup, currently operating at a loss, subject to any corporate tax liabilities?
- What corporate tax responsibilities, if any, apply to our startup consisting of three individuals and presently generating no profit?
- Given our status as a three-person startup with no profit to date, do we have any corporate tax obligations to fulfill?

**Tokens in context:** 915
**Verification modified answer:** False

**Final answer:** As a startup with no profit, you may still have corporate tax obligations. Even if your taxable income is zero, you are required to meet compliance obligations under the Corporate Tax Law. This includes registering for corporate tax purposes, filing a tax return, and retaining all relevant documents and records to support your corporate tax filings. Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 6 [prose] (rerank 0.038, compressed 15→10 sentences) Corporate Tax: The tax imposed by the Corporate Tax Law on juridical persons and Business income. Corporate Tax Law: Federal Decree Law No. 47 of 2022 on the Taxation of Corporations and Businesses. Corporate Tax Payable: Corporate Tax that has or will become due for payment to the FTA in respect of…
- [rank 2] page 19 [prose] (rerank 0.0296, compressed 30→20 sentences) Corporate Tax Law Explanatory Guide on Corporate Tax Law Corporate Tax FAQs Corporate Tax FTA Decisions on the FTA website General Corporate Tax Guide | Corporate Tax | CTGGCT1 4. What is Corporate Tax? This chapter sets out a brief overview of the core principles of Corporate Tax and how the Corpor…
- [rank 3] page 14 [prose] (rerank 0.0261, compressed 20→7 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 This includes what Corporate Tax is, who is subject to Corporate Tax, what types of income are taxable, and how a Taxable Person’s Corporate Tax liability is calculated. Corporate Tax administration process, from Tax Registration and record keepi…
- [rank 4] page 15 [prose] (rerank 0.0138, compressed 26→6 sentences) Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses is referred to as “Corporate Tax Law”; General Corporate Tax Guide | Corporate Tax | CTGGCT1 Are Subject to Corporate Tax is referred to as “Cabinet Decision No. 49 of 2023”; 2022 on the Taxation of Corporations and Bus…
- [rank 5] page 21 [example] (rerank 0.0138, compressed 112→10 sentences) Example 1: Calculation of Corporate Tax A LLC’s Corporate Tax liability will be calculated as follows: • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: Corporate Tax (see Section 7.2) but they will be required to meet the compliance obligations provided for in the Co…

## Q16 — Describe-your-business
**Question:** My mainland trading company made AED 500,000 profit — roughly what do I owe?

**HyDE hypothesis:** Pursuant to the provisions of the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses, a mainland trading company is subject to a corporate tax rate of 9% on taxable profits exceeding AED 375,000. Therefore, on a profit of AED 500,000, the taxable income would be AED 125,000 (i.e., AED 500,000 - AED 375,000), resulting in a corporate tax liability of AED 11,250 (i.e., 9% of AED 125,000).

**Query variants:**
- What is the estimated tax liability for my mainland trading entity, which has reported a profit of AED 500,000?
- Can you provide an approximation of the corporate tax obligation for my mainland trading company with a profit of AED 500,000?
- What would be the anticipated corporate tax due for my mainland trading business based on a profit of AED 500,000?

**Tokens in context:** 1479
**Verification modified answer:** False

**Final answer:** The Corporate Tax rate for a mainland trading company in the UAE is 9% on Taxable Income. Therefore, if your company made a profit of AED 500,000, you would apply the 9% rate to determine the Corporate Tax liability. 

Source: page 111 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 114 [example] (rerank 0.306, compressed 242→15 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax liability was AED 1,000,000. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that woul…
- [rank 2] page 84 [example] (rerank 0.2277, compressed 71→14 sentences) Statements show an Accounting Income of AED 10,000,000. C LLC also has carried forward Tax Losses of AED 2,000,000. • Dividends received from UAE Resident companies: AED 1,000,000; • Income from its Foreign Permanent Establishment in Country B: AED 1,500,000; • Net Interest Expenditure: AED 7,000,00…
- [rank 3] page 80 [example] (rerank 0.1308, compressed 84→17 sentences) In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. LLC has Taxable Income of AED 5,000,000 per year. • In the Tax Period ending on 31 December 2027, C LLC has Taxable Income of AED This means that the maximum Tax Loss that can be used to offset against its Taxable Income…
- [rank 4] page 111 [example] (rerank 0.0842, compressed 84→15 sentences) If three individual companies had Taxable Income each of AED 5,000,000 then each company would pay tax of AED 416,250, a total of AED 1,248,750. Taxable Income (AED) Corporate Tax Payable (AED) Total Corporate Tax due per company Total Corporate Tax Payable for all three companies Income of AED 15,0…
- [rank 5] page 93 [example] (rerank 0.0782, compressed 73→5 sentences) As a result, D LLC sold the machinery to a third party for AED 1,500,000. Value at the date of the transfer, and shall include a gain of AED 400,000 (AED 1,200,000 – AED 800,000) in the Tax Return for the Tax Period in which D LLC subsequently transferred the asset. / loss that will be subject to Co…

## Q17 — Trap / out-of-scope
**Question:** How much VAT do I charge my customers?

**HyDE hypothesis:** In accordance with the Federal Decree-Law No. 8 of 2017 on Value Added Tax, a taxable person must charge a standard VAT rate of 5% on the supply of goods and services, unless a specific exemption or zero-rate applies as stipulated in the relevant provisions of the law. It is imperative that the taxable person issues a tax invoice reflecting the VAT amount charged to ensure compliance with the regulatory requirements set forth by the Federal Tax Authority.

**Query variants:**
- What is the applicable Value Added Tax rate that should be levied on transactions with customers?
- What is the prescribed VAT percentage that must be imposed on the sales to clients?
- What is the statutory rate of Value Added Tax that is required to be charged to customers?

**Tokens in context:** 237
**Verification modified answer:** False

**Final answer:** This is not covered in the provided document. Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 20 [prose] (rerank 0.0038, compressed 7→3 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: General Corporate Tax Guide | Corporate Tax | CTGGCT1 9% (nine percent) on the portion of the Taxable Income exceeding AED
- [rank 2] page 72 [example] (rerank 0.0021, compressed 127→7 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Corporate Tax;199 Recoverable input VAT;200 General Corporate Tax Guide | Corporate Tax | CTGGCT1 General Corporate Tax Guide | Corporate Tax | CTGGCT1 General Corporate Tax Guide | Corporate Tax | CTGGCT1 General Corporate Tax Guide | Corporate …
- [rank 3] page 63 [example] (rerank 0.0016, compressed 29→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1 Corporate Tax purposes. General Corporate Tax Guide | Corporate Tax | CTGGCT1
- [rank 4] page 48 [example] (rerank 0.001, compressed 121→3 sentences) Taxable Income Tax Period The following adjustments should be considered in relation to a Taxable Person’s
- [rank 5] page 111 [example] (rerank 0.0009, compressed 84→3 sentences) Corporate Tax rates for Qualifying Free Zone Persons Withholding Tax rate However, the rate of this tax is 0% meaning that, currently, no tax will need to be withheld.

## Q18 — Trap / out-of-scope
**Question:** What's the corporate tax rate in Saudi Arabia?

**HyDE hypothesis:** As per the prevailing regulations, the corporate tax rate in the Kingdom of Saudi Arabia is set at 20% on the net profits of foreign entities operating within its jurisdiction. Additionally, for wholly owned Saudi companies, the tax rate is applicable to the net profits derived from their business activities, with specific provisions for certain sectors and activities as outlined in the Saudi Income Tax Law.

**Query variants:**
- What is the applicable corporate tax rate in the Kingdom of Saudi Arabia?
- Could you provide the current statutory corporate tax rate enforced in Saudi Arabia?
- What is the prevailing corporate income tax rate established by the authorities in Saudi Arabia?

**Tokens in context:** 1396
**Verification modified answer:** False

**Final answer:** This is not covered in the provided document. Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 21 [example] (rerank 0.4122, compressed 112→20 sentences) Example 1: Calculation of Corporate Tax • The first AED 375,000 of Taxable Income will be subject to Corporate Tax at 0%: Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x A LLC’s UAE Corporate Tax liability for the Tax Period will be AED 506,250. In order to calculate its UA…
- [rank 2] page 60 [example] (rerank 0.213, compressed 74→12 sentences) 160 Article 24(2)(c) of the Corporate Tax Law. 161 Articles 24(4) and 24(5) of the Corporate Tax Law. General Corporate Tax Guide | Corporate Tax | CTGGCT1 Corporate Tax at a rate of more than 9% in their respective countries, the corporate income tax rate in Country C is 5%. General Corporate Tax G…
- [rank 3] page 114 [example] (rerank 0.1623, compressed 242→20 sentences) However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that would have been paid in the UAE on the foreign income (AED 1,500,000 x 9% = AED The amount of Corporate Tax due is therefore AED 1,000,000 – AED 135,000 = AED 360 Article 66 of the Corporate Tax Law. 10. Adminis…
- [rank 4] page 38 [example] (rerank 0.1486, compressed 248→21 sentences) Tax under the general rates, and complies with the transfer pricing rules and other documentation requirements set out in the Corporate Tax Law. 69 Article 17(1) of the Corporate Tax Law and Article 5 of Ministerial Decision No. 127 of 2023. 70 Article 4(1) of the Corporate Tax Law. Activity and wil…
- [rank 5] page 20 [prose] (rerank 0.0744, compressed 7→7 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates: 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law. General Corporate Tax Guide | Co…

## Q19 — Trap / out-of-scope
**Question:** How do I lower the income tax taken from my salary in the UAE?

**HyDE hypothesis:** In the United Arab Emirates, there is currently no federal income tax levied on individual salaries, thereby rendering the question of reducing income tax on salaries moot. However, individuals may optimize their overall tax position by engaging in tax-efficient investment strategies or utilizing available allowances and exemptions under applicable regulations, should they apply to their specific financial circumstances. It is advisable to consult with a qualified tax advisor to explore potential avenues for tax efficiency within the framework of UAE tax law.

**Query variants:**
- What strategies may be employed to mitigate the income tax liability associated with remuneration in the UAE?
- What measures can be implemented to reduce the taxable income derived from salary in the United Arab Emirates?
- In what manner can one optimize the tax obligations related to personal income within the jurisdiction of the UAE?

**Tokens in context:** 1568
**Verification modified answer:** False

**Final answer:** Employment income and other specific types of income earned by natural persons based in the UAE are not within the scope of the UAE Corporate Tax regime. Therefore, there is no income tax on salaries for natural persons in the UAE, and consequently, there is no need to lower income tax taken from a salary. Source: page 21 of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 13 [prose] (rerank 0.0376, compressed 20→8 sentences) Withholding Tax: Corporate Tax to be withheld from State Sourced Income in accordance with Article 45 of the Corporate Tax Law. Withholding Tax Credit: The Corporate Tax amount that can be deducted from the Corporate Tax due in accordance with the conditions of Article 46(2) of the Corporate Federal…
- [rank 2] page 21 [example] (rerank 0.0345, compressed 112→11 sentences) For the purposes of this example, A LLC does not need to make any tax adjustments, thus its Taxable Income will be AED 6 million for the Tax Period. • The portion of the Taxable income exceeding AED 375,000 will be subject to Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x …
- [rank 3] page 114 [example] (rerank 0.0322, compressed 242→8 sentences) During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000 of income it earned in foreign countries. However, the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that would have been paid in the UAE on the foreign income (AED 1,500,000 x 9% = AED Doubl…
- [rank 4] page 12 [prose] (rerank 0.0208, compressed 23→12 sentences) State Sourced Income: Income accruing in, or derived from, the UAE as specified in Article 40(1) of the Corporate Tax Law. Tax purposes with the FTA. Tax Loss: Any negative Taxable Income as calculated under the Corporate Tax Law for a given Tax Period. Tax Registration: A procedure under which a Pe…
- [rank 5] page 26 [example] (rerank 0.01, compressed 298→20 sentences) For natural persons, residence for Corporate Tax purposes is concerned with the person’s business connection to the UAE. It is this connection, rather than other factors such as nationality or where a person is physically present, that gives the UAE the powers to levy Corporate Tax on an individual’…

## Q20 — Trap / out-of-scope
**Question:** Exactly what penalty in AED will I get for filing 47 days late?

**HyDE hypothesis:** In accordance with Article 25 of the Federal Decree-Law No. 47 of 2022 on the Taxation of Corporations and Businesses, a penalty for late filing of a tax return is imposed at a rate of AED 1,000 for the first 30 days of delay, followed by an additional AED 2,000 for each subsequent 30-day period or part thereof. Therefore, for a delay of 47 days, the total penalty incurred will amount to AED 3,000.

**Query variants:**
- What is the specific monetary penalty, expressed in AED, applicable for a late filing of 47 days?
- Could you please specify the financial sanction in AED that will be imposed for a delay of 47 days in submission?
- What is the quantifiable penalty in AED that will be incurred for the submission of documents 47 days past the due date?

**Tokens in context:** 393
**Verification modified answer:** False

**Final answer:** This is not covered in the provided document. Source: page [N] of CTGGCT1.

**Retrieved parents (after reranking + compression):**
- [rank 1] page 20 [prose] (rerank 0.0042, compressed 7→4 sentences) 0% (zero percent) on the portion of the Taxable Income not exceeding AED 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 9% (nine percent) on the portion of the Taxable Income exceeding AED
- [rank 2] page 93 [example] (rerank 0.0037, compressed 73→3 sentences) 1,200,000 – AED 800,000) in the Tax Return for the Tax Period in which D LLC subsequently transferred the asset. / loss that will be subject to Corporate Tax for D LLC, the tax treatment would follow the accounting treatment, meaning that the taxable gain for D LLC will be AED 300,000 (AED 1,500,000…
- [rank 3] page 80 [example] (rerank 0.0036, compressed 84→3 sentences) In the Tax Period ending 31 December 2026 it makes a Tax Loss of AED 6,000,000. • In the Tax Period ending on 31 December 2027, C LLC has Taxable Income of AED In the Tax Period ending on 31 December 2028, C LLC has Taxable Income of AED
- [rank 4] page 86 [example] (rerank 0.0022, compressed 19→3 sentences) In 2025, S LLC sold the Financial Asset for AED 120,000. As a result, S LLC will only need to recognise the gain of AED 20,000 (AED 120,000 – AED 100,000) rather than the full gain of AED 50,000 (AED 120,000 – AED 70,000).
- [rank 5] page 38 [example] (rerank 0.002, compressed 248→3 sentences) 5% of AED 80,000,000 and AED 5,000,000), H LLC will not be eligible to be a Qualifying Tax Period in which the application is made, or from the commencement of a future Tax Period, or any other date determined by the Authority.
