Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable H : V -> (V -> Prop).
  Hypothesis H1 : exists x y : V, H x y \/ H y x.
  Hypothesis H2 : ~ (exists x : V, H x x).
  Lemma ASSG2B_4 : exists x y : V, ~ (x = y).
  Proof.
    unfold not in H2.
    destruct H1 as [a H3].
    destruct H3 as [b H3].
    exists a.
    exists b.
    unfold not.
    intro H4.
    apply H2.
    exists a.
    destruct H3 as [H3_i | H3_ii].
    - rewrite <- H4 in H3_i.
      exact H3_i.
    - rewrite <- H4 in H3_ii.
      exact H3_ii.
  Qed.
