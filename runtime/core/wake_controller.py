# ==========================================
# WAKEWORD CONTROLLER
# Dual Mode:
# 1. Wakeword only → Activate
# 2. Wakeword + command → Execute
# ==========================================

import time


class WakeController:

    def __init__(self,
                 wakeword="सुनो साथी",
                 timeout=8):

        self.wakeword = wakeword
        self.timeout = timeout

        self.active = False
        self.activation_time = 0

    # --------------------------------------

    def process(self, text):
        """
        Returns:
            mode, cleaned_text

        mode:
            "activate"  → wakeword only
            "execute"   → wakeword + command OR active mode command
            None        → ignore
        """

        clean_text = text.strip()
        current_time = time.time()

        # --------------------------------------
        # If already activated (two-step mode)
        # --------------------------------------
        if self.active:

            if current_time - self.activation_time > self.timeout:
                self.active = False
                return None, None

            self.active = False
            return "execute", clean_text

        # --------------------------------------
        # Detect wakeword (minimal tolerance)
        # --------------------------------------

        # Allow:
        # सुनो साथी
        # सुनो साती

        if clean_text.startswith("सुनो साथी") or clean_text.startswith("सुनो साती"):

            if clean_text.startswith("सुनो साती"):
                remaining = clean_text[len("सुनो साती"):].strip()
            else:
                remaining = clean_text[len("सुनो साथी"):].strip()

            # Wakeword + command
            if remaining:
                return "execute", remaining

            # Wakeword only
            self.active = True
            self.activation_time = current_time
            return "activate", None

        return None, None