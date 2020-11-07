Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable S : Prop.
  Variable P : V -> Prop.
  
  Section RightToLeft.
    Hypothesis H1 : (forall x : V, P x) \/ S.
    Lemma ASSG2B_14a : forall x : V, P x \/ S.
    Proof.
      case H1 as [H1_i | H1_ii].
      - intro a.
        pose (H2 := H1_i a).
        left.
        exact H2.
      - intro a.
        right.
        exact H1_ii.
    Qed.
    
  End RightToLeft.

  Section LeftToRight.
    Lemma demorgan : forall p q : Prop, ~ (~p /\ ~q) -> ~ ~ (p \/ q).
    Proof.
      intros p q.
      intro H1.
      unfold not.
      unfold not in H1.
      intro H2.
      apply H1.
      split.
      intro H3.
      apply H2.
      left.
      exact H3.
      intro H3.
      apply H2.
      right.
      exact H3.
    Qed.
    
    Require Import Classical_Prop.
    Hypothesis H1 : forall x : V, P x \/ S.
    Lemma ASSG2B_14b : (forall x : V, P x) \/ S.
    Proof.
      apply NNPP.
      apply demorgan.
      unfold not.
      intro H2.
      destruct H2 as [H2 H3].
      apply H2.
      intro a.
      pose (H4 := H1 a).
      case H4 as [H4_i | H4_ii].
      - exact H4_i.
      - apply H3 in H4_ii.
        elim H4_ii.
    Qed.

    End LeftToRight.
