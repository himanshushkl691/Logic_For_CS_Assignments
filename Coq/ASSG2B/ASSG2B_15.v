Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable S : Prop.
  Variable P : V -> Prop.

  Section LeftToRight.
    Hypothesis H1 : exists x : V, P x /\ S.
    Lemma ASSG2B_15a : (exists x : V, P x) /\ S.
    Proof.
      destruct H1 as [a H2].
      destruct H2 as [H2 H3].
      split.
      exists a.
      exact H2.
      exact H3.
    Qed.
    
  End LeftToRight.

  Section RightToLeft.
    Hypothesis H1 : (exists x : V, P x) /\ S.
    Lemma ASSG2B_15b : exists x : V, P x /\ S.
    Proof.
      destruct H1 as [H2 H3].
      destruct H2 as [a H2].
      exists a.
      split.
      exact H2.
      exact H3.
    Qed.
    
  End RightToLeft.
