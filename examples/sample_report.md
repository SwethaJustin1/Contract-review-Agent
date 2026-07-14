# Contract Review Report: sample_contract.txt

**⚠ ESCALATION RECOMMENDED — one or more high-severity clauses found.**

## Summary
**What this is:** A 2-year agreement where the vendor will provide infrastructure monitoring and incident response services. The contract auto-renews annually unless you cancel with 90 days' notice.

**Your obligations:**
- Pay invoices within 30 days (or face 1.5% monthly interest and possible service suspension after 45 days)
- Protect the vendor's confidential information for 3 years
- Provide 60 days' notice if you want to exit early

**Vendor's obligations:**
- Deliver the services described in Exhibit A (not included here)
- Protect your confidential information
- You'll own any custom work they create once you've paid for it

**Critical issues before signing:**

1. **Review Exhibit A carefully** – the entire scope of work references this missing document. Ensure all deliverables are clearly defined.
2. **Check the indemnification clause** – it appears to require YOU to cover the vendor's legal costs, which seems backwards and may be an error. Get legal review immediately.
3. **Liability cap is very low** – the vendor's maximum liability is only 3 months of fees, which may not cover significant service failures.

## Risk Flags
- **Scope of Services** [MEDIUM] — The scope relies entirely on Exhibit A which is not provided for review, creating uncertainty about actual obligations. → *Review Exhibit A carefully to ensure all deliverables are clearly defined and achievable before signing.*
- **Term** [MEDIUM] — The 90-day notice requirement for non-renewal is lengthy and could lock the vendor into unwanted renewals if not carefully tracked. → *Implement calendar reminders at 120 days before each renewal period or negotiate a shorter notice period of 30-60 days.*
- **Termination** [HIGH] — Client can terminate for convenience with only 60 days notice while vendor has no equivalent right, creating significant business continuity risk. → *Escalate to legal to negotiate mutual termination for convenience rights or minimum revenue guarantees if terminated early.*
- **Payment Terms** [LOW] — Standard net-30 terms with reasonable late payment provisions including interest and service suspension rights protect vendor revenue. → *Acceptable as-is, but ensure invoicing and collections processes can track the 45-day suspension trigger.*
- **Indemnification** [HIGH] — This clause is backwards - it requires the Client to indemnify the Vendor, which is unusual and appears to be an error since we are the vendor. → *Escalate to legal immediately as this clause likely contains an error and should require Vendor to indemnify Client, not vice versa.*
- **Limitation of Liability** [MEDIUM] — The 3-month liability cap is quite low and could be problematic for significant service failures in early contract stages. → *Negotiate to increase the cap to 12 months of fees or annual contract value to better reflect potential damages.*
- **Confidentiality** [LOW] — Mutual confidentiality with reasonable care standard and 3-year post-disclosure term is balanced and standard. → *Acceptable as-is, ensure internal processes exist to mark and protect client confidential information appropriately.*
- **Intellectual Property Ownership** [LOW] — Clear IP ownership with vendor retaining pre-existing IP and client owning paid custom work is fair and standard. → *Acceptable as-is, but ensure Statements of Work clearly define what constitutes custom deliverables versus use of vendor tools.*
- **Governing Law** [LOW] — Delaware law is neutral and well-established for commercial contracts, presenting minimal risk to either party. → *Acceptable as-is unless your organization has strong preference for your home state jurisdiction.*
- **Force Majeure** [LOW] — Standard mutual force majeure clause with typical covered events protects both parties from uncontrollable circumstances. → *Acceptable as-is, though consider whether cyber attacks or pandemics should be explicitly included or excluded.*

## Extracted Clauses
### Scope of Services (Section 1)
Vendor shall provide managed infrastructure monitoring and incident response services as described in Exhibit A, commencing on the Effective Date.

### Term (Section 2)
This Agreement shall remain in effect for twenty-four (24) months from the Effective Date and shall automatically renew for successive twelve (12) month terms unless either party provides written notice of non-renewal at least ninety (90) days prior to the end of the then-current term.

### Termination (Section 2)
Client may terminate this Agreement for convenience with sixty (60) days written notice.

### Payment Terms (Section 3)
Client shall pay Vendor's invoices within thirty (30) days of receipt. Late payments shall accrue interest at 1.5% per month. Vendor reserves the right to suspend services for invoices unpaid beyond forty-five (45) days.

### Indemnification (Section 4)
Client shall indemnify, defend, and hold harmless Vendor, its officers, employees, and agents from and against any and all claims, liabilities, damages, and expenses (including reasonable attorneys' fees) arising out of or related to Client's use of the services, without any cap or limitation on the amount of such indemnification obligation.

### Limitation of Liability (Section 5)
Vendor's total aggregate liability under this Agreement shall not exceed the fees paid by Client in the three (3) months preceding the claim. In no event shall Vendor be liable for indirect, incidental, or consequential damages.

### Confidentiality (Section 6)
Each party agrees to protect the other's confidential information using the same degree of care it uses for its own confidential information, but no less than reasonable care, for a period of three (3) years following disclosure.

### Intellectual Property Ownership (Section 7)
All pre-existing intellectual property of each party remains the property of that party. Any custom deliverables created specifically for Client under a signed Statement of Work shall be owned by Client upon full payment.

### Governing Law (Section 8)
This Agreement shall be governed by the laws of the State of Delaware, without regard to its conflict of laws principles.

### Force Majeure (Section 9)
Neither party shall be liable for delays or failures in performance resulting from acts beyond its reasonable control, including natural disasters, war, or governmental action.
