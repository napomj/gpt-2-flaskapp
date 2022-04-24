#!/usr/bin/env python3

import fire
import json
import os
import numpy as np
import tensorflow.compat.v1 as tf

from flaskapp import model
from flaskapp import sample
from flaskapp import encoder

class AI:
    def generate_text(self, text_input, model_name="124M_bees", length=400):
        seed=None
        nsamples=1
        batch_size=1
        temperature=1
        top_k=40
        top_p=1

        self.response = ""

        currentPath = os.path.dirname(__file__) + "/models" + "/" + model_name

        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        enc = encoder.get_encoder(model_name)
        hparams = model.default_hparams()
        with open(currentPath + '/hparams.json') as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            output = sample.sample_sequence(
                hparams=hparams, length=length,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k, top_p=top_p
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(currentPath)
            saver.restore(sess, ckpt)

            context_tokens = enc.encode(text_input)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    text = enc.decode(out[i])
                    self.response = text
        res = self.response.split('.')
        resStr = ".".join(res[:-1])
        return text_input + resStr + "."

ai = AI()
