# Ring 2 RAG — results to grade

Config: chunk_size=600, overlap=100, cosine_k=20, rerank_k=5, variants=3, token_budget=3000, embed=text-embedding-3-small, chat=gpt-4o-mini

## Q1 — Simple lookup
**Question:** What's the corporate tax rate in the UAE?

**Query variants generated:**
- What is the applicable corporate tax rate imposed within the jurisdiction of the United Arab Emirates?
- Could you provide the current statutory corporate tax rate established in the UAE?
- What is the prevailing rate of corporate taxation as defined under UAE tax legislation?

**Tokens in context:** 562

**Answer:** The corporate tax rate in the UAE is 9% on the portion of the Taxable Income exceeding AED 375,000. Source: page 21 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 21 (rerank 6.0059, compressed 3→3 sentences) • The portion of the Taxable income exceeding AED 375,000 will be subject to  Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x  9% = AED 506,250    A LLC’s UAE Corporate Tax liability for the Tax Period will be AED 506,250. In order to calculate its UAE Corporate Tax payable…
- [rank 2] page 21 (rerank 5.8661, compressed 4→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…
- [rank 3] page 20 (rerank 5.7749, compressed 5→3 sentences) Tax’ or ‘Business Profits Tax’ in other jurisdictions. Corporate Tax is charged on a wide range of Business profits, and those subject to  Corporate Tax in the UAE include not only companies but also certain partnerships,  unincorporated entities and natural persons conducting a Business or Business…
- [rank 4] page 49 (rerank 5.4617, compressed 4→4 sentences) and outside the UAE. •  Non-Resident Persons with a Permanent Establishment or a nexus in the UAE  are subject to Corporate Tax on income attributable to that Permanent  Establishment or nexus. If the Non-Resident does not have a Permanent  Establishment or a nexus in the UAE but derives income from…
- [rank 5] page 113 (rerank 5.0849, compressed 4→3 sentences) extent the income is not attributed to a Permanent Establishment in the UAE. 352  However, the rate of this tax is 0% meaning that, currently, no tax will need to be  withheld. If the rate is changed in future, a Non-Resident Person who becomes subject to  Corporate Tax would be able to reduce their…

## Q2 — Simple lookup
**Question:** When did corporate tax actually start in the UAE?

**Query variants generated:**
- What is the effective commencement date of the corporate tax regime in the United Arab Emirates?
- At what point in time did the implementation of corporate taxation commence within the UAE jurisdiction?
- Can you specify the date on which the corporate tax was officially instituted in the United Arab Emirates?

**Tokens in context:** 562

**Answer:** Corporate Tax in the UAE applies to Tax Periods commencing on or after 1 June 2023. Source: page 14 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 14 (rerank 5.9375, compressed 5→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  13  2. 47 of 2022 on the Taxation of Corporations and Businesses  (“Corporate Tax Law”) was signed on 3 October 2022 and was published in Issue #737  of the Official Gazette of the United Arab Emirates (“UAE”) on 10 October 2022. The Corporate T…
- [rank 2] page 20 (rerank 4.5664, compressed 3→2 sentences) The Financial Year is the period of 12 months for which Financial  Statements are prepared.1 Payment of Corporate Tax is due within nine months from  the end of the applicable Tax Period.2    The UAE Corporate Tax regime applies to Tax Periods commencing on or after 1 June  2023.3      How does Corp…
- [rank 3] page 14 (rerank 4.2328, compressed 3→2 sentences) Purpose of this guide     This guide is designed to provide general guidance on Corporate Tax in the UAE with  a view to making the provisions of the Corporate Tax Law as understandable as  possible to readers. It provides readers with:    • an overview of the main Corporate Tax rules and procedures…
- [rank 4] page 21 (rerank 2.4415, compressed 4→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…
- [rank 5] page 20 (rerank 1.6826, compressed 5→3 sentences) Tax’ or ‘Business Profits Tax’ in other jurisdictions. Corporate Tax is charged on a wide range of Business profits, and those subject to  Corporate Tax in the UAE include not only companies but also certain partnerships,  unincorporated entities and natural persons conducting a Business or Business…

## Q3 — Simple lookup
**Question:** How much profit can I make before I owe any corporate tax?

**Query variants generated:**
- What is the threshold profit amount that triggers the obligation to remit corporate tax?
- What is the minimum profit level at which corporate tax liability arises?
- At what profit point does the duty to pay corporate tax become applicable?

**Tokens in context:** 635

**Answer:** You can make a profit of up to AED 375,000 before owing any corporate tax, as this portion of taxable income is subject to a 0% tax rate. Any taxable income exceeding AED 375,000 will be subject to corporate tax at the applicable rate. 

Source: page 21 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 68 (rerank 0.3737, compressed 4→2 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  67  Example 17: General Interest Deduction Limitation Rule    C LLC has Revenue of AED 150,000,000, adjusted EBITDA of AED 130,000,000 and  Profit Before Tax of AED 60,000,000 for its Financial Year ending 31 December 2025. C LLC may deduct its …
- [rank 2] page 21 (rerank -0.1596, compressed 4→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…
- [rank 3] page 21 (rerank -0.4221, compressed 3→3 sentences) A LLC’s Taxable Income for its Tax Period will be the accounting net profit (or loss) of  the business, after making tax adjustments for certain items specified in the Corporate  Tax Law. For the purposes of this example, A LLC does not need to make any tax  adjustments, thus its Taxable Income will…
- [rank 4] page 88 (rerank -1.8473, compressed 2→2 sentences) Corporate Tax burden and compliance costs in the Corporate Tax regime, primarily by  alleviating the burden of having to calculate and pay Corporate Tax in each relevant  Tax Period where the conditions are satisfied. Any eligible Taxable Person with Revenue equal to or below AED 3,000,000 in a  rel…
- [rank 5] page 79 (rerank -2.2041, compressed 3→3 sentences) Businesses who have a Tax Loss will be able to use the Tax Loss to reduce Taxable  Income in future Tax Periods (provided the necessary conditions are met).228 This is  to ensure that the amount of Corporate Tax paid by Businesses would (subject to  certain conditions) be the same irrespective of wh…

## Q4 — Simple lookup
**Question:** After my financial year ends, how long do I have to file my return?

**Query variants generated:**
- What is the statutory deadline for the submission of my tax return following the conclusion of my financial year?
- What is the prescribed timeframe for filing my tax return subsequent to the end of my financial reporting period?
- What is the mandated period within which I must submit my tax return after the cessation of my financial year?

**Tokens in context:** 580

**Answer:** You have to file your Tax Return and pay Corporate Tax within 9 months from the end of the relevant Tax Period. For example, if your Financial Year ends on 31 December, you are required to file your Tax Return and pay Corporate Tax on or before 30 September the following year. 

Source: page 120 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 120 (rerank 2.9387, compressed 2→2 sentences) of the relevant Tax Period.400 For example, a Taxable Person with a Financial Year  ending on 31 December is required to file their Tax Return and pay Corporate Tax on  or before 30 September the following year. Submitting a Tax Return late or a delay in making a payment of Corporate Tax Payable  wi…
- [rank 2] page 20 (rerank 2.3164, compressed 3→2 sentences) needs to be filed. The Financial Year is the period of 12 months for which Financial  Statements are prepared.1 Payment of Corporate Tax is due within nine months from  the end of the applicable Tax Period.2    The UAE Corporate Tax regime applies to Tax Periods commencing on or after 1 June  2023.3…
- [rank 3] page 120 (rerank 1.6281, kept as-is) •  To move from the Cash Basis of Accounting to Accrual Basis of Accounting;396  •  To form, join or leave a Tax Group, replace a Parent Company in a Tax Group,  or cease to be a Tax Group;397  •  To deregister for Corporate Tax;398 and  •  To change their Tax Period.399     Tax Returns and payments…
- [rank 4] page 50 (rerank -0.1321, compressed 4→3 sentences) Tax Period    A Taxable Person’s (other than a natural person) Tax Period is their Financial Year,  or part thereof, for which a Tax Return is required to be filed.117 This is usually the 12  month period for which they prepare their Financial Statements. If the Taxable Person  does not prepare Fina…
- [rank 5] page 83 (rerank -1.2856, compressed 4→2 sentences) Qualifying Free Zone Persons  and any other Taxable Persons with revenue over AED 50 million must prepare  and maintain audited Financial Statements. •  The second step is to apply the relevant adjustments to the Accounting Income  to arrive at the Taxable Income amount.239    Taxable Persons have t…

## Q5 — Conditional
**Question:** My free-zone company made AED 2 million profit — do I pay 0%?

**Query variants generated:**
- Does the profit of AED 2 million generated by my free-zone entity render it subject to a 0% corporate tax rate?
- Is my free-zone corporation, which has realized a profit of AED 2 million, exempt from corporate taxation at a rate of 0%?
- In light of my free-zone company's profit of AED 2 million, am I liable for corporate tax, or does the 0% rate apply?

**Tokens in context:** 717

**Answer:** To determine if your free-zone company can benefit from the 0% Corporate Tax rate, it is essential to consider whether the profit qualifies as Qualifying Income. If the profit is not considered Qualifying Income, it will be subject to the general tax rate of 9%. Since your profit is AED 2 million, if it is entirely Qualifying Income, you would pay 0%. However, if any portion of it is not Qualifying Income, that portion will be taxed at 9%. 

Source: page 112 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 112 (rerank 0.9797, compressed 5→4 sentences) benefit from the 0% rate. Unlike ordinary Taxable Persons, Qualifying Free Zone Persons are not entitled to a  0% rate on their first AED 375,000 of Taxable Income that is not Qualifying Income. Therefore, any Taxable Income that is not Qualifying Income will be subject to tax at  the general rate o…
- [rank 2] page 33 (rerank 0.0744, compressed 6→3 sentences) 55 of 2023 on Determining Qualifying Income for the  Qualifying Free Zone Person50 and the Ministerial Decision No. Qualifying Income    Qualifying Income is the income that can benefit from the 0% Corporate Tax rate. Unlike ordinary Taxable Persons, Qualifying Free Zone Persons are not entitled to …
- [rank 3] page 21 (rerank -0.2921, compressed 4→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…
- [rank 4] page 38 (rerank -0.7412, compressed 4→3 sentences) During the Tax Period, it undertakes a small number of transactions with individuals  and earns AED 4,500,000 of Revenue. The remaining AED 75,500,000 meets the  requirements to be considered as Qualifying Income. As transactions with individuals are generally Excluded Activities, and Revenue from  …
- [rank 5] page 81 (rerank -1.0297, compressed 5→5 sentences) Taxable Income of AED 5,000,000 in this Tax Period. C LLC will have a final Taxable Income of AED 2,750,000 (AED 5,000,000 – AED  2,250,000). This means that C LLC must pay Corporate Tax of AED 213,750 (AED  375,000 x 0% + AED 2,375,000 x 9%). C LLC will have no Tax Losses to carry forward. (Amounts…

## Q6 — Conditional
**Question:** My business is tiny with very low revenue. Is there relief so I pay nothing?

**Query variants generated:**
- Is there a provision for tax relief applicable to enterprises with minimal revenue, allowing for a zero tax liability?
- Are there any exemptions or relief measures available for small businesses with negligible income that would result in no tax obligation?
- What mechanisms exist within the corporate tax framework to provide relief for businesses with limited revenue, potentially resulting in a nil tax payment?

**Tokens in context:** 532

**Answer:** Yes, if your business is classified as a small business and your Revenue does not exceed the small business relief threshold of AED 3,000,000 per Tax Period, you may be eligible for small business relief. This means you would not need to pay Corporate Tax. However, you must meet the compliance obligations provided for in the Corporate Tax Law for each Tax Period and make an election in your Tax Return to benefit from this relief. Additionally, you cannot be a Constituent Company of a Multinational Enterprise that is required to prepare a full Tax Return. 

Source: page 22 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 89 (rerank -0.758, compressed 5→3 sentences) has never exceeded the small business relief threshold of AED 3,000,000 per Tax  Period in any Tax Period. Mr X is eligible to benefit from small business relief as his Revenue for the 31 December  2025 Tax Period does not exceed AED 3,000,000, which is also the case for previous  years’ Tax Periods…
- [rank 2] page 22 (rerank -0.8502, compressed 4→2 sentences) natural persons, can potentially benefit from small business relief if they meet the  relevant requirements. This means that these businesses would not need to pay  Corporate Tax (see Section 7.2) but they will be required to meet the compliance  obligations provided for in the Corporate Tax Law for…
- [rank 3] page 89 (rerank -1.0407, compressed 6→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  88  For further details on small business relief, readers are advised to consult Ministerial  Decision No. 73 of 2023 on Small Business Relief, and the Corporate Tax Guide on  Small Business Relief. Example 27: Electing for small business relief…
- [rank 4] page 50 (rerank -2.1045, kept as-is) For example, eligible businesses may benefit from small business relief, meaning they  do not need to calculate their Taxable Income and have reduced record keeping  requirements (see Section 7.2).114    Taxable Persons can prepare Financial Statements using the Cash Basis of  Accounting rather than…
- [rank 5] page 88 (rerank -2.1362, compressed 2→2 sentences) be obliged to calculate its Taxable Income or complete a full Tax Return.249 Where a  Taxable Person has elected to benefit from small business relief, they will still be able  to carry forward any unutilised Tax Losses 250  and disallowed Net Interest  Expenditure251 arising from prior Tax Periods …

## Q7 — Conditional
**Question:** My profit is below the threshold — do I still have to register at all?

**Query variants generated:**
- Is it necessary for an entity with profits below the established threshold to complete the registration process?
- Does an organization with earnings that fall beneath the prescribed threshold have an obligation to register?
- Is registration mandated for a taxpayer whose profit does not exceed the specified threshold?

**Tokens in context:** 580

**Answer:** If your profit is below the threshold for Corporate Tax, you may still be required to register if you are considered a Taxable Person. All Taxable Persons must register for Corporate Tax with the FTA and obtain a Tax Registration Number, regardless of their profit level. However, if you are a Non-Resident Person without a Permanent Establishment in the UAE and only earn State Sourced Income, you can choose not to register. If you have a nexus in the UAE, such as earning income from Immovable Property, you are required to register. 

Source: page 116 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 116 (rerank -7.0488, compressed 4→3 sentences) All Taxable Persons should register for Corporate Tax with the FTA and obtain a Tax  Registration Number for Corporate Tax.361 This needs to be done before a deadline to  be determined by the FTA. All Taxable Persons are encouraged to register for  Corporate Tax as soon as they become aware that the…
- [rank 2] page 116 (rerank -7.5444, compressed 2→2 sentences) purposes. However, Non-Resident Persons that have a nexus in the UAE (arising from  earning income from Immovable Property in the UAE – see Section 5.4.4) are required  to register.362    The FTA can, at its discretion, register a Person for Corporate Tax if, on the basis of  information available t…
- [rank 3] page 38 (rerank -7.6005, compressed 4→3 sentences) During the Tax Period, it undertakes a small number of transactions with individuals  and earns AED 4,500,000 of Revenue. The remaining AED 75,500,000 meets the  requirements to be considered as Qualifying Income. As transactions with individuals are generally Excluded Activities, and Revenue from  …
- [rank 4] page 47 (rerank -8.0137, compressed 2→2 sentences) Extractive Businesses and Non-Extractive Natural Resource Businesses to register  with the FTA for Corporate Tax purposes, if they do not have a Business or Business  Activity that is subject to Corporate Tax.109 However, Exempt Persons are required to  maintain records which evidence their exempt s…
- [rank 5] page 89 (rerank -9.1132, compressed 5→3 sentences) has never exceeded the small business relief threshold of AED 3,000,000 per Tax  Period in any Tax Period. Mr X is eligible to benefit from small business relief as his Revenue for the 31 December  2025 Tax Period does not exceed AED 3,000,000, which is also the case for previous  years’ Tax Periods…

## Q8 — Conditional
**Question:** I personally earn rent from a flat I own. Is that taxed?

**Query variants generated:**
- Does the income derived from rental property ownership constitute taxable income under the provisions of the UAE Corporate Tax legislation?
- Is the revenue generated from the leasing of a residential property subject to taxation in accordance with UAE tax regulations?
- Is the rental income received from the ownership of real estate liable for taxation under the applicable corporate tax framework in the UAE?

**Tokens in context:** 370

**Answer:** The income from personal investments, such as rent from a flat owned by a natural person, is not subject to Corporate Tax. This is because such income is considered to be derived from activities undertaken in a personal capacity and not through a commercial business. Therefore, your rental income would not be taxed under the Corporate Tax regime. 

Source: page 28 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 100 (rerank -6.0312, compressed 10→2 sentences) personal travel or home rent given that neither of this expenditure is incurred for the  purposes of the business. 308 Article 16(4)(b) of the Corporate Tax Law.
- [rank 2] page 56 (rerank -7.0444, compressed 7→2 sentences) taxed under the Corporate Tax regime. The income was mainly derived from operating the hotels it owns
- [rank 3] page 99 (rerank -7.5786, compressed 4→2 sentences) Therefore, they are only subject to Corporate Tax on income arising from  categories of Business and Business Activities that are subject to Corporate Tax for  individuals (see Section5.3.3). However, the partners in an Unincorporated Partnership may make an application to  the FTA for the Unincorpo…
- [rank 4] page 28 (rerank -7.8649, compressed 3→2 sentences) it does not include employment, and Corporate Tax does not apply to a natural  person’s salary, wages and other employment income. It also does not include income  from Personal Investments and Real Estate Investments.16    In this regard, Personal Investments are activities that a natural person un…
- [rank 5] page 31 (rerank -8.0722, compressed 4→2 sentences) State Sourced Income may include:  •  income from the sale of goods in the UAE;33  •  income from movable or Immovable Property in the UAE;34 or  •  income from the disposal of shares of a Resident Person.35    In instances where a Non-Resident Person earns State Sourced Income only and  where this …

## Q9 — Multi-hop
**Question:** As a free-zone company, what exactly counts as 'qualifying income' for the 0%?

**Query variants generated:**
- What constitutes 'qualifying income' for the purpose of the 0% tax rate applicable to free-zone entities?
- Could you delineate the parameters that define 'qualifying income' eligible for the 0% corporate tax rate for companies operating within a free zone?
- In the context of free-zone enterprises, what specific revenue streams are classified as 'qualifying income' subject to the 0% tax regime?

**Tokens in context:** 538

**Answer:** Qualifying Income for the 0% Corporate Tax rate includes income earned by Qualifying Free Zone Persons from activities that meet specific criteria outlined in the Corporate Tax Law. For instance, income derived from transactions between Free Zone Persons, such as the sale of Commercial Property located in a Free Zone, can be considered Qualifying Income, provided that all other relevant requirements are met. However, it is important to note that Taxable Income that is not classified as Qualifying Income will be subject to a standard Corporate Tax rate. 

Source: page 38 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 33 (rerank 6.262, compressed 6→5 sentences) 55 of 2023 on Determining Qualifying Income for the  Qualifying Free Zone Person50 and the Ministerial Decision No. 139 of 2023 Regarding  Qualifying Activities and Excluded Activities.51    5.5.1. Qualifying Income    Qualifying Income is the income that can benefit from the 0% Corporate Tax rate. …
- [rank 2] page 32 (rerank 4.8925, compressed 6→3 sentences) Qualifying Income.41 The 0% Corporate Tax rate is available to Qualifying Free Zone                                                  38 Article 1 of Cabinet Decision No. 40 Article 66 of the Corporate Tax Law. 41 Article 3(2)(a) of the Corporate Tax Law.
- [rank 3] page 112 (rerank 4.7206, compressed 3→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  111  9.2.2. Corporate Tax rates for Qualifying Free Zone Persons     Corporate Tax applies to Qualifying Free Zone Persons at the following rates:347    Qualifying Income  0%  Taxable Income that is not Qualifying Income  9%    The Corporate Tax…
- [rank 4] page 23 (rerank 4.6457, compressed 5→2 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  22  A 0% rate of Corporate Tax applies to Qualifying Income earned by certain Free Zone  entities (known as Qualifying Free Zone Persons). The Corporate Tax regime also includes targeted reliefs designed to allow certain  intra-group transaction…
- [rank 5] page 38 (rerank 4.3862, compressed 5→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  37  Example 4: Qualifying Income    F LLC and G LLC are both Free Zone Persons. F LLC (a Qualifying Free Zone Person)  owns a number of warehouses located in a Free Zone. As the transaction  is between two Free Zone Persons, and the sale relates…

## Q10 — Multi-hop
**Question:** Can my group of companies be taxed as one, and what must we meet?

**Query variants generated:**
- Is it permissible for my corporate group to be assessed as a singular taxable entity, and what criteria must be satisfied to qualify for such treatment?
- Can my consortium of enterprises be consolidated for taxation purposes, and what requirements must be fulfilled to achieve this status?
- Is it allowable for my affiliated companies to be taxed collectively, and what conditions must be met to obtain this designation?

**Tokens in context:** 531

**Answer:** Your group of companies can be taxed as one by forming a Tax Group, but you must meet certain conditions. Specifically, you need to make an application to the FTA and receive approval. The Taxable Persons in the group must demonstrate that they meet any necessary criteria, and the FTA may request additional information to make its decision. 

Additionally, the group must consist of companies under common ownership. Once approved, the Tax Group will be treated as a single Taxable Person, which can reduce compliance burdens and increase flexibility in utilizing Tax Losses. 

For further details, you may want to consult the relevant Ministerial Decisions, including Ministerial Decision No. 125 of 2023 on Tax Groups. 

Source: page 119 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 119 (rerank 0.8385, compressed 4→3 sentences) For example, a group of  companies cannot form a Tax Group without having made an application and received  an approval from the FTA.385 Provisions which require a Taxable Person to make an  application cannot take effect until the FTA has approved the application. Taxable Persons will be required t…
- [rank 2] page 23 (rerank 0.6067, compressed 4→2 sentences) Where Persons conduct Business together, either as groups of companies related by  ownership, or as partnerships, special rules may apply for the calculation and payment  of Corporate Tax. Taxable Persons are required to self-assess their Corporate Tax liabilities by  submitting a Tax Return on an a…
- [rank 3] page 110 (rerank 0.3353, compressed 6→5 sentences) to form a single Taxable Person. If individual companies form a Tax Group, or an  Unincorporated Partnership applies to be taxed at the partnership level, only the  Taxable Person (i.e. either the Tax Group or the partnership) will be able to apply the  0% rate to the first AED 375,000 of its collec…
- [rank 4] page 103 (rerank 0.0288, compressed 2→2 sentences) information regarding the partners in the foreign partnership.316    Where these conditions are met, the foreign partnership will be treated as an  Unincorporated Partnership and each of the partners treated as individual Taxable  Persons, unless an application is made to the FTA to be taxed at the …
- [rank 5] page 103 (rerank -0.526, compressed 2→2 sentences) relevant conditions.317 This allows the Tax Group to be treated as a single Taxable  Person, reducing the compliance burden on individual companies by consolidating  accounts and eliminating intra-group transactions, and increasing flexibility in the  utilisation of Tax Losses.318    Businesses and …

## Q11 — Multi-hop
**Question:** My business made a loss last year — can I use it to cut this year's tax?

**Query variants generated:**
- Is it permissible to offset the prior fiscal year's losses against the taxable income of the current fiscal period?
- Can the losses incurred in the preceding financial year be utilized to reduce the taxable liability for the current year?
- Am I allowed to carry forward the losses from the previous year to mitigate the tax obligations for the current assessment period?

**Tokens in context:** 701

**Answer:** Yes, you can use the Tax Loss from last year to reduce this year's Taxable Income, provided you meet certain conditions. Specifically, you must not have elected to benefit from small business relief in the Tax Period in which you incurred the loss. Additionally, you can only offset the Tax Loss against your Taxable Income in subsequent Tax Periods, and the amount of Tax Losses you can use to reduce your Taxable Income is capped at a maximum of 75% of that Taxable Income. 

Source: page 79 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 79 (rerank 1.6519, compressed 3→3 sentences) Businesses who have a Tax Loss will be able to use the Tax Loss to reduce Taxable  Income in future Tax Periods (provided the necessary conditions are met).228 This is  to ensure that the amount of Corporate Tax paid by Businesses would (subject to  certain conditions) be the same irrespective of wh…
- [rank 2] page 79 (rerank 1.5103, compressed 5→5 sentences) Tax Losses    Where a Taxable Person’s deductible expenditure exceeds its income that is subject  to Corporate Tax, it will have negative Taxable Income. This is known as a Tax Loss. Many businesses make losses at some point in their lifecycle. For example, a new  business may initially have losses …
- [rank 3] page 80 (rerank -0.975, compressed 5→5 sentences) use all of the Tax Losses in the current period and cannot choose to carry these Tax  Losses forward.232 Tax Losses cannot be carried back to previous Tax Periods. Example 22: Carried forward Tax Losses    C LLC is a UAE resident company. In the Tax Period ending 31 December 2026 it  makes a Tax Los…
- [rank 4] page 85 (rerank -1.9219, compressed 3→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  84  Add: Entertainment expenditure  250,000  Taxable Income  7,750,000    C LLC can use its carried forward Tax Losses to reduce its Taxable Income by up to  75% of its Taxable Income. As the amount of carried forward Tax Losses of AED  2,000,00…
- [rank 5] page 80 (rerank -2.9281, compressed 4→2 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  79  A Taxable Person cannot claim Tax Losses for the Tax Period in which they have  elected to benefit from small business relief. Tax Loss relief    A Taxable Person can carry forward Tax Losses and offset them against Taxable  Income in subseq…

## Q12 — Multi-hop
**Question:** What records must I keep, and for how long, to stay compliant?

**Query variants generated:**
- What documentation is required to be maintained, and for what duration, to ensure compliance with regulatory obligations?
- What records are mandated for retention, and what is the stipulated retention period to adhere to compliance standards?
- What are the requisite records to be preserved, and what is the prescribed timeframe for such retention to fulfill compliance requirements?

**Tokens in context:** 499

**Answer:** To stay compliant, both Taxable Persons and Exempt Persons must keep records and documents for seven years following the end of the Tax Period to which they relate. 

For Taxable Persons, the records should typically include:
- A record of the Taxable Person’s transactions in the Tax Period.
- A record of the Taxable Person’s assets, including details of any purchases or disposals.
- Order records and delivery notes.
- Other relevant business correspondence.

Exempt Persons must maintain records that enable their exempt status to be readily ascertained by the FTA. The specific documentation required will depend on the reason for their exemption.

The seven-year period starts from the Tax Period in which the invoices or bills were paid, not from when the documents were created. 

Source: page 123 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 123 (rerank 2.6334, compressed 3→2 sentences) Taxable Persons and Exempt Persons must keep records and documents for seven  years following the end of the Tax Period to which they relate.412    This requirement applies to the Tax Period to which the documents relate, and not the  Tax Period in which they were created. In this instance, the seve…
- [rank 2] page 123 (rerank 2.1317, compressed 4→2 sentences) Exempt Persons    Exempt Persons must maintain records that enable the Exempt Person’s status to be  readily ascertained by the FTA.411 The documentation required will depend on the  reason that a Person is exempt from Corporate Tax. How long should records be kept?      Taxable Persons and Exempt P…
- [rank 3] page 47 (rerank -0.2385, compressed 2→2 sentences) Extractive Businesses and Non-Extractive Natural Resource Businesses to register  with the FTA for Corporate Tax purposes, if they do not have a Business or Business  Activity that is subject to Corporate Tax.109 However, Exempt Persons are required to  maintain records which evidence their exempt s…
- [rank 4] page 122 (rerank -2.7514, compressed 4→3 sentences) •  Order records and delivery notes; and  •  Other relevant business correspondence. There is no requirement that these documents are maintained in their original format  and it may be possible to keep them in an alternative format. Failure of a Taxable Person to keep the required records and other …
- [rank 5] page 122 (rerank -2.8032, compressed 3→3 sentences) records or documentation should be maintained, or the format in which they should be  kept. This reflects the fact that the records and documentation required will differ  according to the type and complexity of the Business that the Taxable Person  conducts. Notwithstanding differences between Taxa…

## Q13 — Describe-your-business
**Question:** I freelance from home in Dubai with no trade licence — do I owe corporate tax?

**Query variants generated:**
- Does the absence of a trade license for my freelance activities conducted from my residence in Dubai render me liable for corporate tax obligations?
- Am I subject to corporate tax liabilities given that I operate as a freelancer from my home in Dubai without possessing a trade license?
- In the context of my freelance operations conducted from my domicile in Dubai and the lack of a trade license, am I required to fulfill corporate tax obligations?

**Tokens in context:** 604

**Answer:** If you are a natural person conducting a Business or Business Activity in the UAE, you are considered a Resident Person for Corporate Tax purposes, regardless of your nationality or whether you have a trade license. Therefore, if you are earning income from your freelance activities in Dubai, you would be subject to Corporate Tax on that income. 

Source: page 27 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 49 (rerank -2.3911, compressed 4→4 sentences) and outside the UAE. •  Non-Resident Persons with a Permanent Establishment or a nexus in the UAE  are subject to Corporate Tax on income attributable to that Permanent  Establishment or nexus. If the Non-Resident does not have a Permanent  Establishment or a nexus in the UAE but derives income from…
- [rank 2] page 116 (rerank -3.4651, compressed 4→4 sentences) All Taxable Persons should register for Corporate Tax with the FTA and obtain a Tax  Registration Number for Corporate Tax.361 This needs to be done before a deadline to  be determined by the FTA. All Taxable Persons are encouraged to register for  Corporate Tax as soon as they become aware that the…
- [rank 3] page 30 (rerank -4.0231, compressed 6→4 sentences) Any Person that is a Non-Resident Person and receives State Sourced Income is  subject to Corporate Tax on this income by way of Withholding Tax if the income is  not attributable to a Permanent Establishment of the Non-Resident Person in the  UAE.29                                                  …
- [rank 4] page 116 (rerank -4.119, compressed 2→2 sentences) purposes. However, Non-Resident Persons that have a nexus in the UAE (arising from  earning income from Immovable Property in the UAE – see Section 5.4.4) are required  to register.362    The FTA can, at its discretion, register a Person for Corporate Tax if, on the basis of  information available t…
- [rank 5] page 27 (rerank -4.172, compressed 3→2 sentences) This approach means, for example, that natural persons conducting Businesses or  Business Activities in the UAE are Resident Persons for Corporate Tax irrespective of  their nationality, whether they hold a residency visa in the UAE, whether their income  is sourced in the UAE or from abroad, or how…

## Q14 — Describe-your-business
**Question:** I run a free-zone online store selling to mainland UAE customers — how am I taxed?

**Query variants generated:**
- What are the tax implications for a free-zone e-commerce entity engaging in sales to customers located in mainland UAE?
- What is the applicable tax treatment for a free-zone online retail business transacting with customers in the mainland UAE jurisdiction?
- How is corporate tax assessed on a free-zone online retail operation that conducts sales to clients within the mainland UAE?

**Tokens in context:** 618

**Answer:** To determine how you are taxed as a Free Zone Person running an online store selling to mainland UAE customers, you need to consider the following conditions:

1. **Qualifying Free Zone Person**: You must derive Qualifying Income from relevant transactions, maintain adequate substance in the UAE, satisfy the de minimis requirement, and not have elected to be subject to Corporate Tax under the general rates.

2. **Revenue Threshold**: If your total Revenue exceeds a certain threshold, you may be subject to different tax obligations, including the requirement to prepare and maintain audited Financial Statements.

3. **Tax Return Submission**: You are required to submit a Tax Return to the FTA within a specified timeframe after the end of each Tax Period.

If you meet the criteria for being a Qualifying Free Zone Person and have not elected to be subject to Corporate Tax, you may benefit from certain exemptions. However, if you do not meet these conditions, you may be subject to the Corporate Tax regime.

Source: page 33 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 38 (rerank -0.2677, compressed 4→4 sentences) Example 5: De minimis requirements    H LLC is a Free Zone Person that sells vehicles to other Free Zone Persons. During  the Tax Period it has a total Revenue of AED 80,000,000. H LLC maintains adequate  substance in the Free Zone, has not made an election to be subject to UAE Corporate  Tax under …
- [rank 2] page 56 (rerank -1.3332, compressed 7→6 sentences) taxed under the Corporate Tax regime. This exemption also covers distributions made  by a Resident Free Zone juridical person (whether qualifying or not) to another  Resident Person. Example 10: Distributions received from a juridical person that is a Resident  Person    C LLC owns and operates a ho…
- [rank 3] page 33 (rerank -2.1326, kept as-is) General Corporate Tax Guide | Corporate Tax | CTGGCT1  32  Persons until the expiry of the tax incentive period provided for in the legislation of the  relevant Free Zone (unless renewed).42    In order to be considered as a Qualifying Free Zone Person, a Free Zone Person must  meet the following re…
- [rank 4] page 25 (rerank -2.6581, compressed 4→4 sentences) separate legal personality under the applicable UAE mainland legislation or Free Zone  regulations. UAE branches of a domestic or foreign juridical person are regarded as  an extension of their head office and, therefore, are not considered separate juridical  persons.13    5.3.2. Effective manageme…
- [rank 5] page 83 (rerank -2.9504, compressed 4→3 sentences) This will be  based on Financial Statements prepared according to accounting standards  recognised in the UAE (IFRS or IFRS for SMEs). Qualifying Free Zone Persons  and any other Taxable Persons with revenue over AED 50 million must prepare  and maintain audited Financial Statements. •  The second s…

## Q15 — Describe-your-business
**Question:** We're a 3-person startup with no profit yet. Any corporate tax obligations?

**Query variants generated:**
- Does our three-member startup, currently operating at a loss, incur any corporate tax liabilities?
- What are the corporate tax obligations applicable to our startup, consisting of three individuals and presently not generating profit?
- Is our three-person startup, which has yet to realize any profits, subject to any corporate tax requirements?

**Tokens in context:** 551

**Answer:** As a startup with no profit, you may still have corporate tax obligations. If your Revenue is equal to or below AED 3,000,000 in a relevant Tax Period and all previous Tax Periods (ending on or before 31 December 2026), you can elect to be treated as having no Taxable Income in that period. This means you would not be obliged to calculate your Taxable Income or complete a full Tax Return. However, you will still need to meet compliance obligations, including registering for Corporate Tax purposes, filing a Tax Return, and retaining relevant documents and records to support your Corporate Tax filings. 

Source: page 88 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 88 (rerank -4.5732, compressed 2→2 sentences) Corporate Tax burden and compliance costs in the Corporate Tax regime, primarily by  alleviating the burden of having to calculate and pay Corporate Tax in each relevant  Tax Period where the conditions are satisfied. Any eligible Taxable Person with Revenue equal to or below AED 3,000,000 in a  rel…
- [rank 2] page 57 (rerank -5.001, kept as-is) General Corporate Tax Guide | Corporate Tax | CTGGCT1  56    •  The Taxable Person has an ownership interest of 5% or greater in the shares  or capital of the Participation which has been held, or is intended to be held, for  a period of at least 12 months;140  •  The Taxable Person is entitled to a…
- [rank 3] page 22 (rerank -5.0991, compressed 4→3 sentences) natural persons, can potentially benefit from small business relief if they meet the  relevant requirements. This means that these businesses would not need to pay  Corporate Tax (see Section 7.2) but they will be required to meet the compliance  obligations provided for in the Corporate Tax Law for…
- [rank 4] page 47 (rerank -5.6678, compressed 6→4 sentences) subject to the obligations set out in the Corporate Tax Law, including, for example, to  register for Corporate Tax and file a Tax Return in relation to their taxable Business or  Business Activity.112                                                          108 Article 10(1)(c) of the Corporate Tax…
- [rank 5] page 23 (rerank -6.5778, compressed 4→2 sentences) Where Persons conduct Business together, either as groups of companies related by  ownership, or as partnerships, special rules may apply for the calculation and payment  of Corporate Tax. Taxable Persons are required to self-assess their Corporate Tax liabilities by  submitting a Tax Return on an a…

## Q16 — Describe-your-business
**Question:** My mainland trading company made AED 500,000 profit — roughly what do I owe?

**Query variants generated:**
- What is the estimated tax liability for my mainland trading entity with a profit of AED 500,000?
- Could you provide an approximation of the corporate tax obligation for my mainland trading company, given a profit of AED 500,000?
- What would be the anticipated corporate tax due for my mainland trading business reporting a profit of AED 500,000?

**Tokens in context:** 652

**Answer:** To determine the Corporate Tax liability for your mainland trading company with a profit of AED 500,000, you need to consider the applicable tax rate. The Corporate Tax is 9% on the portion of the Taxable Income exceeding AED 375,000. 

In this case, the Taxable Income of AED 500,000 exceeds AED 375,000 by AED 125,000. Therefore, the Corporate Tax would be calculated on this excess amount. 

The specific amount owed will depend on the calculation based on the tax rate applied to the excess. 

Source: page 21 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 114 (rerank -2.7913, compressed 6→3 sentences) C LLC is a UAE resident company that does business through Permanent  Establishments in a number of foreign countries. During the Tax Period, C LLC paid AED 300,000 in foreign taxes on the AED 1,500,000  of income it earned in foreign countries. At the end of the Tax Period, C LLC’s Corporate Tax li…
- [rank 2] page 84 (rerank -2.9561, compressed 4→3 sentences) C LLC also has carried forward Tax Losses of AED 2,000,000. Its Accounting Income for the most recent Tax Period includes the following items:  • Dividends received from UAE Resident companies: AED 1,000,000;  • Income from its Foreign Permanent Establishment in Country B: AED 1,500,000;  • Net Inte…
- [rank 3] page 83 (rerank -3.1604, compressed 4→3 sentences) This gives F LLC a final Taxable Income of AED 500,000. The remaining AED 500,000  of unutilised losses is carried forward by C LLC to the subsequent Tax Period. (Amounts in AED)  C LLC  F LLC  Taxable Income / (Loss)  (2,000,000)  2,000,000  Tax Loss transferred   1,500,000  0  Tax Losses received …
- [rank 4] page 70 (rerank -3.2233, compressed 5→5 sentences) Expenditure is then reduced to AED 5,000,000 (AED 7,500,000 – AED 2,500,000). The  maximum amount M LLC can claim as a deduction for Net Interest Expenditure in the  Tax Period ending December 2026 is AED 16,500,000. Given that the Net Interest Expenditure is AED 14,000,000, and M LLC was allowed to…
- [rank 5] page 21 (rerank -3.8834, compressed 4→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…

## Q17 — Trap / out-of-scope
**Question:** How much VAT do I charge my customers?

**Query variants generated:**
- What is the applicable Value Added Tax rate that should be levied on my clientele?
- What is the prescribed VAT percentage that I am obligated to impose on my customers?
- What is the statutory VAT rate that must be applied to transactions with my customers?

**Tokens in context:** 300

**Answer:** This is not covered in the provided document.  
Source: page 4 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 4 (rerank -8.9217, compressed 8→2 sentences) General tax rates ......................................................................................... Corporate Tax rates for Qualifying Free Zone Persons ...............................
- [rank 2] page 4 (rerank -9.4674, compressed 9→2 sentences) How is any Corporate Tax liability calculated? ........... 109    Applicable Corporate Tax rates ..........................................................................
- [rank 3] page 73 (rerank -9.5874, kept as-is) General Corporate Tax Guide | Corporate Tax | CTGGCT1  72  •  Dividends, profit distributions or benefits of a similar nature paid to an owner of  the Taxable Person;197  •  Amounts withdrawn from the Business by a natural person who is a Taxable  Person or a partner in an Unincorporated Partnership…
- [rank 4] page 20 (rerank -10.7308, compressed 4→2 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates:  •  0% (zero percent) on the portion of the Taxable Income not exceeding AED  375,000. 3 Article 69 of the Corporate Tax Law.
- [rank 5] page 64 (rerank -10.7625, compressed 5→2 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  63  Throughout the Tax Period, Mr A recorded the mileage of his business and personal  journeys. Mr A’s Accounting Income for the Tax Period is AED 4,500,000

## Q18 — Trap / out-of-scope
**Question:** What's the corporate tax rate in Saudi Arabia?

**Query variants generated:**
- What is the applicable corporate tax rate in the Kingdom of Saudi Arabia?
- Could you provide the current statutory corporate tax rate enforced in Saudi Arabia?
- What is the prevailing corporate income tax rate as stipulated by the regulations in Saudi Arabia?

**Tokens in context:** 550

**Answer:** This is not covered in the provided document. Source: page 20 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 20 (rerank -0.3377, compressed 5→3 sentences) Tax’ or ‘Business Profits Tax’ in other jurisdictions. Corporate Tax is charged on a wide range of Business profits, and those subject to  Corporate Tax in the UAE include not only companies but also certain partnerships,  unincorporated entities and natural persons conducting a Business or Business…
- [rank 2] page 21 (rerank -0.9904, compressed 4→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  20  •  9% (nine percent) on the portion of the Taxable Income exceeding AED  375,000. Example 1: Calculation of Corporate Tax    A LLC is a company incorporated in the UAE. In the Tax Period ending March 2025, A  LLC generated Revenue of AED 8 m…
- [rank 3] page 20 (rerank -1.3088, compressed 4→4 sentences) Generally, Corporate Tax is imposed on Taxable Income at the following rates:  •  0% (zero percent) on the portion of the Taxable Income not exceeding AED  375,000. 1 Article 57 of the Corporate Tax Law. 2 Article 48 of the Corporate Tax Law. 3 Article 69 of the Corporate Tax Law.
- [rank 4] page 21 (rerank -1.7127, compressed 3→3 sentences) • The portion of the Taxable income exceeding AED 375,000 will be subject to  Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x  9% = AED 506,250    A LLC’s UAE Corporate Tax liability for the Tax Period will be AED 506,250. In order to calculate its UAE Corporate Tax payable…
- [rank 5] page 14 (rerank -1.7334, compressed 5→4 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  13  2. 47 of 2022 on the Taxation of Corporations and Businesses  (“Corporate Tax Law”) was signed on 3 October 2022 and was published in Issue #737  of the Official Gazette of the United Arab Emirates (“UAE”) on 10 October 2022. The Corporate T…

## Q19 — Trap / out-of-scope
**Question:** How do I lower the income tax taken from my salary in the UAE?

**Query variants generated:**
- What measures can be undertaken to minimize the income tax liability associated with salary remuneration in the UAE?
- What strategies are available for the reduction of income tax obligations arising from salary earnings within the UAE jurisdiction?
- In what ways can one legally mitigate the income tax assessed on salary income in the United Arab Emirates?

**Tokens in context:** 526

**Answer:** This is not covered in the provided document.  
Source: page [N] of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 113 (rerank 1.2333, compressed 4→4 sentences) extent the income is not attributed to a Permanent Establishment in the UAE. 352  However, the rate of this tax is 0% meaning that, currently, no tax will need to be  withheld. If the rate is changed in future, a Non-Resident Person who becomes subject to  Corporate Tax would be able to reduce their…
- [rank 2] page 114 (rerank 1.0427, compressed 6→3 sentences) LLC can reduce its Corporate Tax liability using available Foreign Tax Credit. However,  the amount of Foreign Tax Credit is limited to the amount of Corporate Tax that would  have been paid in the UAE on the foreign income (AED 1,500,000 x 9% = AED                                                  3…
- [rank 3] page 49 (rerank 0.5512, compressed 3→3 sentences) their Business or Business Activity derived from the UAE, or from outside the  UAE if it is connected to the Business or Business Activity being carried out in  the UAE. Taxable Income is determined by applying the adjustments set out in Section 6.2.2 to  a Taxable Person’s annual Accounting Income,…
- [rank 4] page 21 (rerank 0.1066, compressed 3→2 sentences) • The portion of the Taxable income exceeding AED 375,000 will be subject to  Corporate Tax at 9%: (AED 6,000,000 - AED 375,000) x 9% = AED 5,625,000 x  9% = AED 506,250    A LLC’s UAE Corporate Tax liability for the Tax Period will be AED 506,250. In order to calculate its UAE Corporate Tax payable…
- [rank 5] page 114 (rerank -0.1715, compressed 4→2 sentences) In order to apply Foreign Tax Credit, the pre-tax foreign income must be included in  the Taxable Income of the UAE Resident Person. The amount of Corporate Tax due  should be calculated based on the overall Taxable Income, and Foreign Tax Credit  can then be deducted from the amount of Corporate Ta…

## Q20 — Trap / out-of-scope
**Question:** Exactly what penalty in AED will I get for filing 47 days late?

**Query variants generated:**
- What is the specific monetary penalty, expressed in AED, applicable for a late filing of 47 days?
- What is the prescribed financial sanction in AED for the submission of tax documents 47 days beyond the stipulated deadline?
- Could you delineate the exact penalty in AED that will be imposed for a delay of 47 days in filing?

**Tokens in context:** 620

**Answer:** For filing a Tax Return 47 days late, the penalty will be calculated based on the rules for late submissions. The first twelve months of delay incur a penalty of AED 500 for each month or part thereof. Since 47 days is more than one month but less than two months, you will incur a penalty of AED 500 for the first month. Therefore, the total penalty for filing 47 days late will be AED 500. 

Source: page 120 of CTGGCT1.

**Retrieved + compressed chunks:**
- [rank 1] page 120 (rerank 1.6811, compressed 2→2 sentences) of the relevant Tax Period.400 For example, a Taxable Person with a Financial Year  ending on 31 December is required to file their Tax Return and pay Corporate Tax on  or before 30 September the following year. Submitting a Tax Return late or a delay in making a payment of Corporate Tax Payable  wi…
- [rank 2] page 117 (rerank -0.7516, compressed 4→3 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  116  Failure to submit a deregistration application within 3 months of the date the entity  ceases to exist, cessation of the Business, dissolution, liquidation or otherwise, will  result in a penalty of AED 1,000, and a further AED 1,000 on the…
- [rank 3] page 123 (rerank -4.9102, compressed 4→2 sentences) General Corporate Tax Guide | Corporate Tax | CTGGCT1  122  •  AED 10,000 for each violation;  •  AED 20,000 in each case of repeated violation within 24 months from the date  of the last violation.410    10.7.1. How long should records be kept?      Taxable Persons and Exempt Persons must keep reco…
- [rank 4] page 81 (rerank -6.6971, compressed 5→4 sentences) Taxable Income of AED 5,000,000 in this Tax Period. C LLC will have a final Taxable Income of AED 2,750,000 (AED 5,000,000 – AED  2,250,000). This means that C LLC must pay Corporate Tax of AED 213,750 (AED  375,000 x 0% + AED 2,375,000 x 9%). (Amounts in AED)  31/12/2026  31/12/2027  31/12/2028  Ta…
- [rank 5] page 70 (rerank -7.1948, kept as-is) The remaining carried forward Net Interest Expenditure amount of AED 5,000,000 can  be carried forward and deducted in the subsequent 10 Tax Periods after the interest  expenditure arose in the order in which the amount was incurred and subject to the
