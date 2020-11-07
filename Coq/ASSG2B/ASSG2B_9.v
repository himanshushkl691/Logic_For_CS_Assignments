Require Import Classical_Prop.
Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q R : V -> Prop.
  Hypothesis H1 : forall x : V, P x -> (Q x \/ R x).
  Hypothesis H2 : ~ exists x : V, P x /\ R x.
  Lemma ASSG2B_9 : forall x : V, P x -> Q x.
  Proof.
    unfold not in H2.
    intro a.
    intro H3.
    pose (H4 := H1 a).
    apply NNPP.
    unfold not.
    intro H5.
    apply H2.
    exists a.
    split.
    exact H3.
    apply H4 in H3.
    case H3 as [H3_i | H3_ii].
    + apply H5 in H3_i.
      elim H3_i.
    + exact H3_ii.
  Qed.
  
