Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q R : V -> Prop.
  Hypothesis H1 : forall x : V, Q x -> R x.
  Hypothesis H2 : exists x : V, P x /\ Q x.
  Lemma ASSG2B_2 : exists x : V, P x /\ R x.
  Proof.
    destruct H2 as [a H3].
    destruct H3 as [H3 H4].
    exists a.
    split.
    exact H3.
    pose (H5 := H1 a).
    apply H5.
    exact H4.
  Qed.
