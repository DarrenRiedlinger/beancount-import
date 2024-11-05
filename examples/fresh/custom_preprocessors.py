"""
Tamplate for defining custom preprocessors that can match certain transactions and
process them deterministically.

A list of preprocessor functions can be passed to the webserver using the 
'transaction_preprocessors' key. E.g.
beancount_import.webserver.main(
        # ... normal options
        transaction_preprocessors = [my_custom_preprocessor, my_other_processor]
        )

Each transaction_preprocessor function should take a beancount Transaction, and return
a PreprocessorResult composed of an optionally new, modified transaction and an action.
Thi can result in 4 different program behavious:

1) If the returned transaction is None, this preprocessor is skipped.
   Any remaining transaction_preprocessors will try to match the original transaction
   If none return a transaction, normal source importing and interactive matching continues.
Else:

2) If action=='ignore', the returned transaction is written to the ignore journal
   The transaciton will no longer appear as a pending transaction in the web-ui.
   Any remaining preprocessors are skipped
3) If action=='record', the returned transaciton is written directly to the 
   configured output journal. The transaction will no longer appear as a pending
   transaction in the web-ui.
   Any remaining preprocessors are skipped
4) If action=='continue', the returned transaction (potentially modified) will
   not be directly written to the ledger. It will instead appear as a pending
   transaciton in the web-ui.
   Any remaining preprocessors are skipped
"""

from beancount.core.data import Transaction
import beancount.parser.printer
import ipdb; ipdb.set_trace()
from beancount_import.reconcile import PreprocessorResult

def my_custom_preprocessor(transaction: Transaction) -> PreprocessorResult:
    """Handle specific transaction patterns."""
    import ipdb; ipdb.set_trace()
    if "PATTERN" in transaction.narration:
        modified = transaction._replace(
            narration="Modified " + transaction.narration
        )
        return PreprocessorResult(transaction=modified, action="record")
    return PreprocessorResult(transaction=None, action="continue")

